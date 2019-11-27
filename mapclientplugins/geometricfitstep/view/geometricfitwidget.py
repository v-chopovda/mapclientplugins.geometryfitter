"""
User interface for github.com/ABI-Software/scaffoldfitter
"""
from PySide import QtGui, QtCore

from mapclientplugins.geometricfitstep.view.ui_geometricfitwidget import Ui_GeometricFitWidget
from opencmiss.zinc.scene import Scene
from scaffoldfitter.fitterstepalign import FitterStepAlign
from scaffoldfitter.fitterstepfit import FitterStepFit
from scaffoldfitter.utils.zinc_utils import FieldIsCoordinateCapable


def QLineEdit_parseVector3(lineedit):
    """
    Return 3 component real vector as list from comma separated text in QLineEdit widget
    or None if invalid.
    """
    try:
        text = lineedit.text()
        values = [ float(value) for value in text.split(',') ]
        if len(values) == 3:
            return values
    except:
        pass
    return None

def QLineEdit_parseRealNonNegative(lineedit):
    """
    Return non-negative real value from line edit text, or negative if failed.
    """
    try:
        value = float(lineedit.text())
        if value >= 0.0:
            return value
    except:
        pass
    return -1.0

class GeometricFitWidget(QtGui.QWidget):
    """
    User interface for github.com/ABI-Software/scaffoldfitter
    """

    def __init__(self, model, parent=None):
        """
        """
        super(GeometricFitWidget, self).__init__(parent)
        self._ui = Ui_GeometricFitWidget()
        self._ui.setupUi(self)
        self._ui.alignmentsceneviewerwidget.setContext(model.getContext())
        self._ui.alignmentsceneviewerwidget.setModel(model)
        self._model = model
        self._fitter = self._model.getFitter()
        self._context = self._fitter.getContext()
        self._region = self._fitter.getRegion()
        self._scene = self._region.getScene()
        self._currentFitterStep = None  # Current FitterStep being edited; None = Fitter config
        self._ui.alignmentsceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)
        self._callback = None
        self._setupConfigWidgets()
        self._updateGeneralWidgets()
        self._updateConfigWidgets()
        self._updateDisplayWidgets()
        self._model.createGraphics()
        self._makeConnections()

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        Set custom scene from model
        """
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setScene(self._model.getScene())
            sceneviewer.viewAll()

    def _makeConnections(self):
        self._makeConnectionsGeneral()
        self._makeConnectionsDisplay()
        self._makeConnectionsConfig()
        self._makeConnectionsAlign()
        self._makeConnectionsFit()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _autoPerturbLines(self):
        """
        Enable scene viewer perturb lines iff solid surfaces are drawn with lines.
        Call whenever lines, surfaces or translucency changes
        """
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setPerturbLinesFlag(self._model.needPerturbLines())

# === general widgets ===

    def _makeConnectionsGeneral(self):
        self._ui.stepsAddAlign_pushButton.clicked.connect(self._stepsAddAlignClicked)
        self._ui.stepsAddFit_pushButton.clicked.connect(self._stepsAddFitClicked)
        self._ui.stepsDelete_pushButton.clicked.connect(self._stepsDeleteClicked)
        self._ui.steps_listView.clicked.connect(self._stepsListItemClicked)
        self._ui.done_pushButton.clicked.connect(self._doneClicked)
        self._ui.viewAll_pushButton.clicked.connect(self._viewAllClicked)

    def _updateGeneralWidgets(self):
        self._ui.identifier_label.setText('Identifier:  ' + self._model.getIdentifier())
        self._buildStepsList()

    def _stepsAddAlignClicked(self):
        """
        Add a new align step.
        """
        self._currentFitterStep = FitterStepAlign(self._fitter)
        self._buildStepsList()

    def _stepsAddFitClicked(self):
        """
        Add a new fit step.
        """
        self._currentFitterStep = FitterStepFit(self._fitter)
        self._buildStepsList()

    def _stepsDeleteClicked(self):
        """
        Delete the currently selected step, except for config.
        Select next step after, or before if none.
        """
        #print("_stepsDeleteClicked")
        destroyFitterStep = self._currentFitterStep
        if destroyFitterStep:
            self._currentFitterStep = self._fitter.getNextFitterStep(self._currentFitterStep)
            destroyFitterStep.destroy()
            self._buildStepsList()

    def _stepsListItemClicked(self):
        """
        Changes current step and possibly changes checked/run status.
        """
        modelIndex = self._ui.steps_listView.currentIndex()
        model = modelIndex.model()
        item = model.item(modelIndex.row())
        #print("_stepsListItemClicked", item.checkState() == QtCore.Qt.Checked)
        step = item.data()
        self._currentFitterStep = step
        self._updateFitterStepWidgets()
        #visibilityFlag = item.checkState() == QtCore.Qt.Checked
        #graphics.setVisibilityFlag(visibilityFlag)
        #selectedModelIndex = self._ui.steps_listView.currentIndex()
        #selectedItem = model.item(selectedModelIndex.row())
        #selectedGraphics = selectedItem.data()
        #if graphics == selectedGraphics:
        #    self._ui.graphics_editor.setGraphics(selectedGraphics)

    def _buildStepsList(self):
        '''
        Fill the graphics list view with the list of graphics for current region/scene
        '''
        #GRC store in self?
        self._stepsItems = QtGui.QStandardItemModel(self._ui.steps_listView)
        selectedIndex = None
        fitter = self._model.getFitter()
        # fitter configuration appears as first step called "Config"
        item = QtGui.QStandardItem("Config")
        item.setData(None)
        item.setCheckable(True)
        item.setEditable(False)
        self._stepsItems.appendRow(item)
        selectedIndex = self._stepsItems.indexFromItem(item)
        for step in fitter.getFitterSteps():
            name = None
            isAlign = isinstance(step, FitterStepAlign)
            isFit = isinstance(step, FitterStepFit)
            assert isAlign or isFit, "GeometricFitWidget.  Unknown FitterStep type"
            name = "Align" if isAlign else "Fit"
            item = QtGui.QStandardItem(name)
            item.setData(step)
            item.setCheckable(True)
            item.setEditable(False)
            item.setCheckState(QtCore.Qt.Checked if step.hasRun() else QtCore.Qt.Unchecked)
            self._stepsItems.appendRow(item)
            if step == self._currentFitterStep:
                selectedIndex = self._stepsItems.indexFromItem(item)
        self._ui.steps_listView.setModel(self._stepsItems)
        self._ui.steps_listView.setCurrentIndex(selectedIndex)
        self._ui.steps_listView.show()
        self._updateFitterStepWidgets()

    def _updateFitterStepWidgets(self):
        """
        Update and display widgets for currentFitterStep
        """
        if self._currentFitterStep is None:
            self._ui.config_groupBox.show()
            self._ui.align_groupBox.hide()
            self._ui.fit_groupBox.hide()
        elif isinstance(self._currentFitterStep, FitterStepAlign):
            self._updateAlignWidgets()
            self._ui.config_groupBox.hide()
            self._ui.align_groupBox.show()
            self._ui.fit_groupBox.hide()
        else:  # elif isinstance(self._currentFitterStep, FitterStepFit):
            self._updateFitWidgets()
            self._ui.config_groupBox.hide()
            self._ui.align_groupBox.hide()
            self._ui.fit_groupBox.show()
        self._ui.stepsDelete_pushButton.setEnabled(self._currentFitterStep is not None)

    def _doneClicked(self):
        self._model.setStatePostAlign() # ensure model is transformed; does nothing if not in align tab
        self._model.writeOutputModel()
        #sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        #sceneviewer.setScene(Scene())
        self._ui.dockWidget.setFloating(False)
        self._callback()

    def _viewAllClicked(self):
        self._ui.alignmentsceneviewerwidget.viewAll()

# === display widgets ===

    def _makeConnectionsDisplay(self):
        self._ui.displayAxes_checkBox.clicked.connect(self._displayAxesClicked)
        self._ui.displayElementAxes_checkBox.clicked.connect(self._displayElementAxesClicked)
        self._ui.displayElementNumbers_checkBox.clicked.connect(self._displayElementNumbersClicked)
        self._ui.displayLines_checkBox.clicked.connect(self._displayLinesClicked)
        self._ui.displayLinesExterior_checkBox.clicked.connect(self._displayLinesExteriorClicked)
        self._ui.displayNodeDerivativeLabelsD1_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD1Clicked)
        self._ui.displayNodeDerivativeLabelsD2_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD2Clicked)
        self._ui.displayNodeDerivativeLabelsD3_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD3Clicked)
        self._ui.displayNodeDerivativeLabelsD12_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD12Clicked)
        self._ui.displayNodeDerivativeLabelsD13_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD13Clicked)
        self._ui.displayNodeDerivativeLabelsD23_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD23Clicked)
        self._ui.displayNodeDerivativeLabelsD123_checkBox.clicked.connect(self._displayNodeDerivativeLabelsD123Clicked)
        self._ui.displayNodeDerivatives_checkBox.clicked.connect(self._displayNodeDerivativesClicked)
        self._ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbersClicked)
        self._ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePointsClicked)
        self._ui.displaySurfaces_checkBox.clicked.connect(self._displaySurfacesClicked)
        self._ui.displaySurfacesExterior_checkBox.clicked.connect(self._displaySurfacesExteriorClicked)
        self._ui.displaySurfacesTranslucent_checkBox.clicked.connect(self._displaySurfacesTranslucentClicked)
        self._ui.displaySurfacesWireframe_checkBox.clicked.connect(self._displaySurfacesWireframeClicked)

    def _updateDisplayWidgets(self):
        """
        Update display widgets to display settings for model graphics display.
        """
        self._ui.displayAxes_checkBox.setChecked(self._model.isDisplayAxes())
        self._ui.displayNodePoints_checkBox.setChecked(self._model.isDisplayNodePoints())
        self._ui.displayNodeNumbers_checkBox.setChecked(self._model.isDisplayNodeNumbers())
        self._ui.displayNodeDerivativeLabelsD1_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D1'))
        self._ui.displayNodeDerivativeLabelsD2_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D2'))
        self._ui.displayNodeDerivativeLabelsD3_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D3'))
        self._ui.displayNodeDerivativeLabelsD12_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D12'))
        self._ui.displayNodeDerivativeLabelsD13_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D13'))
        self._ui.displayNodeDerivativeLabelsD23_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D23'))
        self._ui.displayNodeDerivativeLabelsD123_checkBox.setChecked(self._model.isDisplayNodeDerivativeLabels('D123'))
        self._ui.displayNodeDerivatives_checkBox.setChecked(self._model.isDisplayNodeDerivatives())
        self._ui.displayElementNumbers_checkBox.setChecked(self._model.isDisplayElementNumbers())
        self._ui.displayElementAxes_checkBox.setChecked(self._model.isDisplayElementAxes())
        self._ui.displayLines_checkBox.setChecked(self._model.isDisplayLines())
        self._ui.displayLinesExterior_checkBox.setChecked(self._model.isDisplayLinesExterior())
        self._ui.displaySurfaces_checkBox.setChecked(self._model.isDisplaySurfaces())
        self._ui.displaySurfacesExterior_checkBox.setChecked(self._model.isDisplaySurfacesExterior())
        self._ui.displaySurfacesTranslucent_checkBox.setChecked(self._model.isDisplaySurfacesTranslucent())
        self._ui.displaySurfacesWireframe_checkBox.setChecked(self._model.isDisplaySurfacesWireframe())

    def _displayAxesClicked(self):
        self._model.setDisplayAxes(self._ui.displayAxes_checkBox.isChecked())

    def _displayNodePointsClicked(self):
        self._model.setDisplayNodePoints(self._ui.displayNodePoints_checkBox.isChecked())

    def _displayNodeNumbersClicked(self):
        self._model.setDisplayNodeNumbers(self._ui.displayNodeNumbers_checkBox.isChecked())

    def _displayNodeDerivativesClicked(self):
        self._model.setDisplayNodeDerivatives(self._ui.displayNodeDerivatives_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD1Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D1', self._ui.displayNodeDerivativeLabelsD1_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD2Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D2', self._ui.displayNodeDerivativeLabelsD2_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD3Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D3', self._ui.displayNodeDerivativeLabelsD3_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD12Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D12', self._ui.displayNodeDerivativeLabelsD12_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD13Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D13', self._ui.displayNodeDerivativeLabelsD13_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD23Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D23', self._ui.displayNodeDerivativeLabelsD23_checkBox.isChecked())

    def _displayNodeDerivativeLabelsD123Clicked(self):
        self._model.setDisplayNodeDerivativeLabels('D123', self._ui.displayNodeDerivativeLabelsD123_checkBox.isChecked())

    def _displayElementAxesClicked(self):
        self._model.setDisplayElementAxes(self._ui.displayElementAxes_checkBox.isChecked())

    def _displayElementNumbersClicked(self):
        self._model.setDisplayElementNumbers(self._ui.displayElementNumbers_checkBox.isChecked())

    def _displayLinesClicked(self):
        self._model.setDisplayLines(self._ui.displayLines_checkBox.isChecked())
        self._autoPerturbLines()

    def _displayLinesExteriorClicked(self):
        self._model.setDisplayLinesExterior(self._ui.displayLinesExterior_checkBox.isChecked())

    def _displaySurfacesClicked(self):
        self._model.setDisplaySurfaces(self._ui.displaySurfaces_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesExteriorClicked(self):
        self._model.setDisplaySurfacesExterior(self._ui.displaySurfacesExterior_checkBox.isChecked())

    def _displaySurfacesTranslucentClicked(self):
        self._model.setDisplaySurfacesTranslucent(self._ui.displaySurfacesTranslucent_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesWireframeClicked(self):
        self._model.setDisplaySurfacesWireframe(self._ui.displaySurfacesWireframe_checkBox.isChecked())

# === config widgets ===

    def _setupConfigWidgets(self):
        """
        Set up config widgets and display values from fitter object.
        """
        self._ui.configModelCoordinates_fieldChooser.setRegion(self._region)
        self._ui.configModelCoordinates_fieldChooser.setNullObjectName('-')
        self._ui.configModelCoordinates_fieldChooser.setConditional(FieldIsCoordinateCapable)
        self._ui.configDataCoordinates_fieldChooser.setRegion(self._region)
        self._ui.configDataCoordinates_fieldChooser.setNullObjectName('-')
        self._ui.configDataCoordinates_fieldChooser.setConditional(FieldIsCoordinateCapable)

    def _updateConfigWidgets(self):
        """
        Update config widgets to display settings for Fitter.
        """
        self._ui.configModelCoordinates_fieldChooser.setField(self._fitter.getModelCoordinatesField())
        self._ui.configDataCoordinates_fieldChooser.setField(self._fitter.getDataCoordinatesField())

    def _makeConnectionsConfig(self):
        #QtCore.QObject.connect(self.coordinate_field_chooser, QtCore.SIGNAL("currentIndexChanged(int)"), GraphicsEditorWidget.coordinateFieldChanged)
        self._ui.configModelCoordinates_fieldChooser.currentIndexChanged.connect(self._configModelCoordinatesFieldChanged)
        self._ui.configDataCoordinates_fieldChooser.currentIndexChanged.connect(self._configDataCoordinatesFieldChanged)

    def _configModelCoordinatesFieldChanged(self, index):
        """
        Callback for change in model coordinates field chooser widget.
        """
        field = self._ui.configModelCoordinates_fieldChooser.getField()
        if field:
            self._fitter.setModelCoordinatesField(field)

    def _configDataCoordinatesFieldChanged(self, index):
        """
        Callback for change in data coordinates field chooser widget.
        """
        field = self._ui.configDataCoordinates_fieldChooser.getField()
        if field:
            self._fitter.setDataCoordinatesField(field)

# === align widgets ===

    def _makeConnectionsAlign(self):
        self._ui.alignMarkers_checkBox.clicked.connect(self._alignMarkersClicked)
        self._ui.alignRotation_lineEdit.editingFinished.connect(self._alignRotationEntered)
        self._ui.alignScale_lineEdit.editingFinished.connect(self._alignScaleEntered)
        self._ui.alignTranslation_lineEdit.editingFinished.connect(self._alignTranslationEntered)

    def _getAlign(self):
        align = self._currentFitterStep
        assert isinstance(align, FitterStepAlign)
        return align

    def _updateAlignWidgets(self):
        """
        Update align widgets to display parameters from current align step.
        """
        align = self._getAlign()
        realFormat = "{:.4g}"
        self._ui.alignMarkers_checkBox.setCheckState(QtCore.Qt.Checked if align.isAlignMarkers() else QtCore.Qt.Unchecked)
        self._ui.alignRotation_lineEdit.setText(", ".join(realFormat.format(value) for value in align.getRotation()))
        self._ui.alignScale_lineEdit.setText(realFormat.format(align.getScale()))
        self._ui.alignTranslation_lineEdit.setText(", ".join(realFormat.format(value) for value in align.getTranslation()))

    def _alignMarkersClicked(self):
        state = self._ui.alignMarkers_checkBox.checkState()
        self._getAlign().setAlignMarkers(state == QtCore.Qt.Checked)

    def _alignRotationEntered(self):
        values = QLineEdit_parseVector3(self._ui.alignRotation_lineEdit)
        if values:
            self._getAlign().setRotation(values)
        else:
            print("Invalid model rotation Euler angles entered")
            self._updateAlignWidgets()

    def _alignScaleEntered(self):
        value = QLineEdit_parseRealNonNegative(self._ui.alignScale_lineEdit)
        if value > 0.0:
            self._getAlign().setScale(value)
        else:
            print("Invalid model scale entered")
            self._updateAlignWidgets()

    def _alignTranslationEntered(self):
        values = QLineEdit_parseVector3(self._ui.alignTranslation_lineEdit)
        if values:
            self._getAlign().setTranslation(values)
        else:
            print("Invalid model translation entered")
            self._updateAlignWidgets()

# === fit widgets ===

    def _makeConnectionsFit(self):
        self._ui.fitStrainPenalty_lineEdit.editingFinished.connect(self._fitStrainPenaltyEntered)
        self._ui.fitCurvaturePenalty_lineEdit.editingFinished.connect(self._fitCurvaturePenaltyEntered)
        self._ui.fitEdgeDiscontinuityPenalty_lineEdit.editingFinished.connect(self._fitEdgeDiscontinuityPenaltyEntered)
        self._ui.fitIterations_spinBox.valueChanged.connect(self._fitIterationsValueChanged)
        self._ui.fitUpdateReferenceState_checkBox.clicked.connect(self._fitUpdateReferenceStateClicked)

    def _getFit(self):
        assert isinstance(self._currentFitterStep, FitterStepFit)
        return self._currentFitterStep

    def _updateFitWidgets(self):
        """
        Update fit widgets to display parameters from fit step.
        """
        fit = self._getFit()
        realFormat = "{:.4g}"
        self._ui.fitStrainPenalty_lineEdit.setText(realFormat.format(fit.getStrainPenaltyWeight()))
        self._ui.fitCurvaturePenalty_lineEdit.setText(realFormat.format(fit.getCurvaturePenaltyWeight()))
        self._ui.fitEdgeDiscontinuityPenalty_lineEdit.setText(realFormat.format(fit.getEdgeDiscontinuityPenaltyWeight()))
        self._ui.fitIterations_spinBox.setValue(fit.getNumberOfIterations())
        self._ui.fitUpdateReferenceState_checkBox.setCheckState(QtCore.Qt.Checked if fit.isUpdateReferenceState() else QtCore.Qt.Unchecked)

    def _fitStrainPenaltyEntered(self):
        value = QLineEdit_parseRealNonNegative(self._ui.fitStrainPenalty_lineEdit)
        if value >= 0.0:
            self._getFit().setStrainPenaltyWeight(value)
        else:
            print("Invalid penalty weight; must be non-negative")
            self._updateFitWidgets()

    def _fitCurvaturePenaltyEntered(self):
        value = QLineEdit_parseRealNonNegative(self._ui.fitCurvaturePenalty_lineEdit)
        if value >= 0.0:
            self._getFit().setCurvaturePenaltyWeight(value)
        else:
            print("Invalid penalty weight; must be non-negative")
            self._updateFitWidgets()

    def _fitEdgeDiscontinuityPenaltyEntered(self):
        value = QLineEdit_parseRealNonNegative(self._ui.fitEdgeDiscontinuityPenalty_lineEdit)
        if value >= 0.0:
            self._getFit().setEdgeDiscontinuityPenaltyWeight(value)
        else:
            print("Invalid penalty weight; must be non-negative")
            self._updateFitWidgets()

    def _fitIterationsValueChanged(self, value):
        self._getFit().setNumberOfIterations(value)

    def _fitUpdateReferenceStateClicked(self):
        state = self._ui.fitUpdateReferenceState_checkBox.checkState()
        self._getFit().setUpdateReferenceState(state == QtCore.Qt.Checked)
