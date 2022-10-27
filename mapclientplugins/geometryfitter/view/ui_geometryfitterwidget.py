# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometryfitterwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget
from opencmiss.zincwidgets.fieldchooserwidget import FieldChooserWidget
from opencmiss.zincwidgets.draggablelistwidget import DraggableListWidget


class Ui_GeometryFitterWidget(object):
    def setupUi(self, GeometryFitterWidget):
        if not GeometryFitterWidget.objectName():
            GeometryFitterWidget.setObjectName(u"GeometryFitterWidget")
        GeometryFitterWidget.resize(1718, 1365)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeometryFitterWidget.sizePolicy().hasHeightForWidth())
        GeometryFitterWidget.setSizePolicy(sizePolicy)
        GeometryFitterWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(GeometryFitterWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(GeometryFitterWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.identifier_label = QLabel(self.dockWidgetContents)
        self.identifier_label.setObjectName(u"identifier_label")
        sizePolicy.setHeightForWidth(self.identifier_label.sizePolicy().hasHeightForWidth())
        self.identifier_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.identifier_label)

        self.steps_groupBox = QGroupBox(self.dockWidgetContents)
        self.steps_groupBox.setObjectName(u"steps_groupBox")
        sizePolicy.setHeightForWidth(self.steps_groupBox.sizePolicy().hasHeightForWidth())
        self.steps_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.steps_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stepsAddDelete_frame = QFrame(self.steps_groupBox)
        self.stepsAddDelete_frame.setObjectName(u"stepsAddDelete_frame")
        self.stepsAddDelete_frame.setFrameShape(QFrame.StyledPanel)
        self.stepsAddDelete_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.stepsAddDelete_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stepsAddAlign_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddAlign_pushButton.setObjectName(u"stepsAddAlign_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddAlign_pushButton)

        self.stepsAddConfig_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddConfig_pushButton.setObjectName(u"stepsAddConfig_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddConfig_pushButton)

        self.stepsAddFit_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddFit_pushButton.setObjectName(u"stepsAddFit_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddFit_pushButton)

        self.stepsDelete_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsDelete_pushButton.setObjectName(u"stepsDelete_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsDelete_pushButton)


        self.verticalLayout_2.addWidget(self.stepsAddDelete_frame)

        self.steps_listWidget = DraggableListWidget(self.steps_groupBox)
        self.steps_listWidget.setObjectName(u"steps_listWidget")

        self.verticalLayout_2.addWidget(self.steps_listWidget)

        self.stepedit_scrollArea = QScrollArea(self.steps_groupBox)
        self.stepedit_scrollArea.setObjectName(u"stepedit_scrollArea")
        sizePolicy.setHeightForWidth(self.stepedit_scrollArea.sizePolicy().hasHeightForWidth())
        self.stepedit_scrollArea.setSizePolicy(sizePolicy)
        self.stepedit_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stepedit_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.stepedit_scrollArea.setWidgetResizable(True)
        self.stepedit_scrollAreaWidgetContents = QWidget()
        self.stepedit_scrollAreaWidgetContents.setObjectName(u"stepedit_scrollAreaWidgetContents")
        self.stepedit_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 598, 956))
        self.verticalLayout_3 = QVBoxLayout(self.stepedit_scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.configInitial_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.configInitial_groupBox.setObjectName(u"configInitial_groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.configInitial_groupBox.sizePolicy().hasHeightForWidth())
        self.configInitial_groupBox.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.configInitial_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.configModelCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configModelCoordinates_label.setObjectName(u"configModelCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configModelCoordinates_label)

        self.configModelCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configModelCoordinates_fieldChooser.setObjectName(u"configModelCoordinates_fieldChooser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.configModelCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelCoordinates_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configModelCoordinates_fieldChooser)

        self.configModelFitGrouplabel = QLabel(self.configInitial_groupBox)
        self.configModelFitGrouplabel.setObjectName(u"configModelFitGrouplabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configModelFitGrouplabel)

        self.configModelFitGroup_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configModelFitGroup_fieldChooser.setObjectName(u"configModelFitGroup_fieldChooser")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configModelFitGroup_fieldChooser)

        self.configFlattenGroup_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configFlattenGroup_fieldChooser.setObjectName(u"configFlattenGroup_fieldChooser")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configFlattenGroup_fieldChooser)

        self.configFlattenGroup_label = QLabel(self.configInitial_groupBox)
        self.configFlattenGroup_label.setObjectName(u"configFlattenGroup_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configFlattenGroup_label)

        self.configFibreOrientation_label = QLabel(self.configInitial_groupBox)
        self.configFibreOrientation_label.setObjectName(u"configFibreOrientation_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configFibreOrientation_label)

        self.configFibreOrientation_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configFibreOrientation_fieldChooser.setObjectName(u"configFibreOrientation_fieldChooser")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configFibreOrientation_fieldChooser)

        self.configDataCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy3.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)

        self.configDiagnosticLevel_label = QLabel(self.configInitial_groupBox)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configMarkerGroup_label = QLabel(self.configInitial_groupBox)
        self.configMarkerGroup_label.setObjectName(u"configMarkerGroup_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.configMarkerGroup_label)

        self.configMarkerGroup_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configMarkerGroup_fieldChooser.setObjectName(u"configMarkerGroup_fieldChooser")
        sizePolicy3.setHeightForWidth(self.configMarkerGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configMarkerGroup_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.configMarkerGroup_fieldChooser)

        self.configDiagnosticLevel_spinBox = QSpinBox(self.configInitial_groupBox)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)


        self.verticalLayout_3.addWidget(self.configInitial_groupBox)

        self.config_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.config_groupBox.setObjectName(u"config_groupBox")
        sizePolicy.setHeightForWidth(self.config_groupBox.sizePolicy().hasHeightForWidth())
        self.config_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.config_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.config_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.config_verticalSpacer)


        self.verticalLayout_3.addWidget(self.config_groupBox)

        self.align_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.align_groupBox.setObjectName(u"align_groupBox")
        sizePolicy.setHeightForWidth(self.align_groupBox.sizePolicy().hasHeightForWidth())
        self.align_groupBox.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.align_groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.alignGroups_checkBox = QCheckBox(self.align_groupBox)
        self.alignGroups_checkBox.setObjectName(u"alignGroups_checkBox")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.alignGroups_checkBox)

        self.alignMarkers_checkBox = QCheckBox(self.align_groupBox)
        self.alignMarkers_checkBox.setObjectName(u"alignMarkers_checkBox")
        sizePolicy.setHeightForWidth(self.alignMarkers_checkBox.sizePolicy().hasHeightForWidth())
        self.alignMarkers_checkBox.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.alignMarkers_checkBox)

        self.alignRotation_label = QLabel(self.align_groupBox)
        self.alignRotation_label.setObjectName(u"alignRotation_label")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.alignRotation_label)

        self.alignRotation_lineEdit = QLineEdit(self.align_groupBox)
        self.alignRotation_lineEdit.setObjectName(u"alignRotation_lineEdit")
        sizePolicy3.setHeightForWidth(self.alignRotation_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignRotation_lineEdit.setSizePolicy(sizePolicy3)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.alignRotation_lineEdit)

        self.alignScale_label = QLabel(self.align_groupBox)
        self.alignScale_label.setObjectName(u"alignScale_label")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.alignScale_label)

        self.alignScale_lineEdit = QLineEdit(self.align_groupBox)
        self.alignScale_lineEdit.setObjectName(u"alignScale_lineEdit")
        sizePolicy3.setHeightForWidth(self.alignScale_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignScale_lineEdit.setSizePolicy(sizePolicy3)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.alignScale_lineEdit)

        self.alignTranslation_label = QLabel(self.align_groupBox)
        self.alignTranslation_label.setObjectName(u"alignTranslation_label")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.alignTranslation_label)

        self.alignTranslation_lineEdit = QLineEdit(self.align_groupBox)
        self.alignTranslation_lineEdit.setObjectName(u"alignTranslation_lineEdit")
        sizePolicy3.setHeightForWidth(self.alignTranslation_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignTranslation_lineEdit.setSizePolicy(sizePolicy3)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.alignTranslation_lineEdit)


        self.verticalLayout_3.addWidget(self.align_groupBox)

        self.fit_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.fit_groupBox.setObjectName(u"fit_groupBox")
        sizePolicy.setHeightForWidth(self.fit_groupBox.sizePolicy().hasHeightForWidth())
        self.fit_groupBox.setSizePolicy(sizePolicy)
        self.fit_groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fit_groupBox.setFlat(False)
        self.fit_groupBox.setCheckable(False)
        self.formLayout_3 = QFormLayout(self.fit_groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.fitIterations_label = QLabel(self.fit_groupBox)
        self.fitIterations_label.setObjectName(u"fitIterations_label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.fitIterations_label)

        self.fitIterations_spinBox = QSpinBox(self.fit_groupBox)
        self.fitIterations_spinBox.setObjectName(u"fitIterations_spinBox")
        sizePolicy3.setHeightForWidth(self.fitIterations_spinBox.sizePolicy().hasHeightForWidth())
        self.fitIterations_spinBox.setSizePolicy(sizePolicy3)
        self.fitIterations_spinBox.setMinimum(1)
        self.fitIterations_spinBox.setMaximum(1000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.fitIterations_spinBox)

        self.fitMaximumSubIterations_label = QLabel(self.fit_groupBox)
        self.fitMaximumSubIterations_label.setObjectName(u"fitMaximumSubIterations_label")
        self.fitMaximumSubIterations_label.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.fitMaximumSubIterations_label)

        self.fitMaximumSubIterations_spinBox = QSpinBox(self.fit_groupBox)
        self.fitMaximumSubIterations_spinBox.setObjectName(u"fitMaximumSubIterations_spinBox")
        self.fitMaximumSubIterations_spinBox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.fitMaximumSubIterations_spinBox.sizePolicy().hasHeightForWidth())
        self.fitMaximumSubIterations_spinBox.setSizePolicy(sizePolicy3)
        self.fitMaximumSubIterations_spinBox.setMinimum(1)
        self.fitMaximumSubIterations_spinBox.setMaximum(1000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.fitMaximumSubIterations_spinBox)

        self.fitUpdateReferenceState_checkBox = QCheckBox(self.fit_groupBox)
        self.fitUpdateReferenceState_checkBox.setObjectName(u"fitUpdateReferenceState_checkBox")
        sizePolicy.setHeightForWidth(self.fitUpdateReferenceState_checkBox.sizePolicy().hasHeightForWidth())
        self.fitUpdateReferenceState_checkBox.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.fitUpdateReferenceState_checkBox)


        self.verticalLayout_3.addWidget(self.fit_groupBox)

        self.groupSettings_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.groupSettings_groupBox.setObjectName(u"groupSettings_groupBox")
        sizePolicy2.setHeightForWidth(self.groupSettings_groupBox.sizePolicy().hasHeightForWidth())
        self.groupSettings_groupBox.setSizePolicy(sizePolicy2)
        self.groupSettings_Layout = QFormLayout(self.groupSettings_groupBox)
        self.groupSettings_Layout.setObjectName(u"groupSettings_Layout")
        self.groupSettings_Layout.setContentsMargins(-1, -1, -1, 0)
        self.groupSettings_label = QLabel(self.groupSettings_groupBox)
        self.groupSettings_label.setObjectName(u"groupSettings_label")

        self.groupSettings_Layout.setWidget(1, QFormLayout.LabelRole, self.groupSettings_label)

        self.groupSettings_fieldChooser = FieldChooserWidget(self.groupSettings_groupBox)
        self.groupSettings_fieldChooser.setObjectName(u"groupSettings_fieldChooser")
        sizePolicy3.setHeightForWidth(self.groupSettings_fieldChooser.sizePolicy().hasHeightForWidth())
        self.groupSettings_fieldChooser.setSizePolicy(sizePolicy3)

        self.groupSettings_Layout.setWidget(1, QFormLayout.FieldRole, self.groupSettings_fieldChooser)

        self.groupConfigCentralProjection_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupConfigCentralProjection_checkBox.setObjectName(u"groupConfigCentralProjection_checkBox")

        self.groupSettings_Layout.setWidget(2, QFormLayout.LabelRole, self.groupConfigCentralProjection_checkBox)

        self.groupConfigSetCentralProjection_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupConfigSetCentralProjection_checkBox.setObjectName(u"groupConfigSetCentralProjection_checkBox")

        self.groupSettings_Layout.setWidget(2, QFormLayout.FieldRole, self.groupConfigSetCentralProjection_checkBox)

        self.groupConfigDataProportion_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupConfigDataProportion_checkBox.setObjectName(u"groupConfigDataProportion_checkBox")

        self.groupSettings_Layout.setWidget(3, QFormLayout.LabelRole, self.groupConfigDataProportion_checkBox)

        self.groupConfigDataProportion_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupConfigDataProportion_lineEdit.setObjectName(u"groupConfigDataProportion_lineEdit")

        self.groupSettings_Layout.setWidget(3, QFormLayout.FieldRole, self.groupConfigDataProportion_lineEdit)

        self.groupFitDataWeight_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupFitDataWeight_checkBox.setObjectName(u"groupFitDataWeight_checkBox")

        self.groupSettings_Layout.setWidget(4, QFormLayout.LabelRole, self.groupFitDataWeight_checkBox)

        self.groupFitDataWeight_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupFitDataWeight_lineEdit.setObjectName(u"groupFitDataWeight_lineEdit")

        self.groupSettings_Layout.setWidget(4, QFormLayout.FieldRole, self.groupFitDataWeight_lineEdit)

        self.groupFitStrainPenalty_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupFitStrainPenalty_checkBox.setObjectName(u"groupFitStrainPenalty_checkBox")

        self.groupSettings_Layout.setWidget(5, QFormLayout.LabelRole, self.groupFitStrainPenalty_checkBox)

        self.groupFitStrainPenalty_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupFitStrainPenalty_lineEdit.setObjectName(u"groupFitStrainPenalty_lineEdit")

        self.groupSettings_Layout.setWidget(5, QFormLayout.FieldRole, self.groupFitStrainPenalty_lineEdit)

        self.groupFitCurvaturePenalty_checkBox = QCheckBox(self.groupSettings_groupBox)
        self.groupFitCurvaturePenalty_checkBox.setObjectName(u"groupFitCurvaturePenalty_checkBox")

        self.groupSettings_Layout.setWidget(6, QFormLayout.LabelRole, self.groupFitCurvaturePenalty_checkBox)

        self.groupFitCurvaturePenalty_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupFitCurvaturePenalty_lineEdit.setObjectName(u"groupFitCurvaturePenalty_lineEdit")

        self.groupSettings_Layout.setWidget(6, QFormLayout.FieldRole, self.groupFitCurvaturePenalty_lineEdit)


        self.verticalLayout_3.addWidget(self.groupSettings_groupBox)

        self.stepedit_scrollArea.setWidget(self.stepedit_scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.stepedit_scrollArea)


        self.verticalLayout.addWidget(self.steps_groupBox)

        self.controls_tabWidget = QTabWidget(self.dockWidgetContents)
        self.controls_tabWidget.setObjectName(u"controls_tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.controls_tabWidget.sizePolicy().hasHeightForWidth())
        self.controls_tabWidget.setSizePolicy(sizePolicy4)
        self.display_tab = QWidget()
        self.display_tab.setObjectName(u"display_tab")
        self.verticalLayout_7 = QVBoxLayout(self.display_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_tab)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displayMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.displayMisc_horizontalSpacer)

        self.displayGroup_label = QLabel(self.displayMisc_frame)
        self.displayGroup_label.setObjectName(u"displayGroup_label")

        self.horizontalLayout_8.addWidget(self.displayGroup_label)

        self.displayGroup_fieldChooser = FieldChooserWidget(self.displayMisc_frame)
        self.displayGroup_fieldChooser.setObjectName(u"displayGroup_fieldChooser")
        sizePolicy3.setHeightForWidth(self.displayGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.displayGroup_fieldChooser.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.displayGroup_fieldChooser)


        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayMarker_frame = QFrame(self.display_tab)
        self.displayMarker_frame.setObjectName(u"displayMarker_frame")
        self.displayMarker_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMarker_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.displayMarker_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.displayMarkerDataNames_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerDataNames_checkBox.setObjectName(u"displayMarkerDataNames_checkBox")

        self.gridLayout.addWidget(self.displayMarkerDataNames_checkBox, 0, 1, 1, 1)

        self.displayMarkerDataPoints_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerDataPoints_checkBox.setObjectName(u"displayMarkerDataPoints_checkBox")

        self.gridLayout.addWidget(self.displayMarkerDataPoints_checkBox, 0, 0, 1, 1)

        self.displayMarkerNames_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerNames_checkBox.setObjectName(u"displayMarkerNames_checkBox")

        self.gridLayout.addWidget(self.displayMarkerNames_checkBox, 3, 1, 1, 1)

        self.displayMarkerPoints_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerPoints_checkBox.setObjectName(u"displayMarkerPoints_checkBox")

        self.gridLayout.addWidget(self.displayMarkerPoints_checkBox, 3, 0, 1, 1)

        self.displayMarkerDataProjections_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerDataProjections_checkBox.setObjectName(u"displayMarkerDataProjections_checkBox")

        self.gridLayout.addWidget(self.displayMarkerDataProjections_checkBox, 0, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.displayMarker_frame)

        self.displayData_frame = QFrame(self.display_tab)
        self.displayData_frame.setObjectName(u"displayData_frame")
        self.displayData_frame.setFrameShape(QFrame.StyledPanel)
        self.displayData_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayData_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.displayDataPoints_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataPoints_checkBox.setObjectName(u"displayDataPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataPoints_checkBox)

        self.displayDataProjections_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataProjections_checkBox.setObjectName(u"displayDataProjections_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataProjections_checkBox)

        self.displayDataProjectionPoints_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataProjectionPoints_checkBox.setObjectName(u"displayDataProjectionPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayDataProjectionPoints_checkBox)

        self.displayData_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.displayData_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayData_frame)

        self.displayNodes_frame = QFrame(self.display_tab)
        self.displayNodes_frame.setObjectName(u"displayNodes_frame")
        self.displayNodes_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNodes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNodes_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNodePoints_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodePoints_checkBox.setObjectName(u"displayNodePoints_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeNumbers_checkBox.setObjectName(u"displayNodeNumbers_checkBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.displayNodeNumbers_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeNumbers_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodeDerivatives_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeDerivatives_checkBox.setObjectName(u"displayNodeDerivatives_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivatives_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivatives_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.displayNodeDerivatives_checkBox)

        self.displayNodes_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.displayNodes_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayNodes_frame)

        self.displayNodeDerivativeLabels_frame = QFrame(self.display_tab)
        self.displayNodeDerivativeLabels_frame.setObjectName(u"displayNodeDerivativeLabels_frame")
        self.displayNodeDerivativeLabels_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNodeDerivativeLabels_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.displayNodeDerivativeLabels_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.displayNodeDerivativeLabels_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.displayNodeDerivativeLabels_horizontalSpacer)

        self.displayNodeDerivativeLabelsD1_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD1_checkBox.setObjectName(u"displayNodeDerivativeLabelsD1_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD1_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD1_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD1_checkBox)

        self.displayNodeDerivativeLabelsD2_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD2_checkBox.setObjectName(u"displayNodeDerivativeLabelsD2_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD2_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD2_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD2_checkBox)

        self.displayNodeDerivativeLabelsD3_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD3_checkBox.setObjectName(u"displayNodeDerivativeLabelsD3_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD3_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD3_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD3_checkBox)

        self.displayNodeDerivativeLabelsD12_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD12_checkBox.setObjectName(u"displayNodeDerivativeLabelsD12_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD12_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD12_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD12_checkBox)

        self.displayNodeDerivativeLabelsD13_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD13_checkBox.setObjectName(u"displayNodeDerivativeLabelsD13_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD13_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD13_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD13_checkBox)

        self.displayNodeDerivativeLabelsD23_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD23_checkBox.setObjectName(u"displayNodeDerivativeLabelsD23_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD23_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD23_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD23_checkBox)

        self.displayNodeDerivativeLabelsD123_checkBox = QCheckBox(self.displayNodeDerivativeLabels_frame)
        self.displayNodeDerivativeLabelsD123_checkBox.setObjectName(u"displayNodeDerivativeLabelsD123_checkBox")
        sizePolicy5.setHeightForWidth(self.displayNodeDerivativeLabelsD123_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivativeLabelsD123_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.displayNodeDerivativeLabelsD123_checkBox)


        self.verticalLayout_7.addWidget(self.displayNodeDerivativeLabels_frame)

        self.displayElements_frame = QFrame(self.display_tab)
        self.displayElements_frame.setObjectName(u"displayElements_frame")
        self.displayElements_frame.setFrameShape(QFrame.StyledPanel)
        self.displayElements_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.displayElements_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayElementNumbers_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementNumbers_checkBox.setObjectName(u"displayElementNumbers_checkBox")

        self.horizontalLayout_4.addWidget(self.displayElementNumbers_checkBox)

        self.displayElementAxes_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementAxes_checkBox.setObjectName(u"displayElementAxes_checkBox")
        sizePolicy5.setHeightForWidth(self.displayElementAxes_checkBox.sizePolicy().hasHeightForWidth())
        self.displayElementAxes_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.displayElementAxes_checkBox)

        self.displayElements_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.displayElements_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayElements_frame)

        self.displayLines_frame = QFrame(self.display_tab)
        self.displayLines_frame.setObjectName(u"displayLines_frame")
        self.displayLines_frame.setFrameShape(QFrame.StyledPanel)
        self.displayLines_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.displayLines_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.displayLines_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLines_checkBox.setObjectName(u"displayLines_checkBox")

        self.horizontalLayout_5.addWidget(self.displayLines_checkBox)

        self.displayLinesExterior_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLinesExterior_checkBox.setObjectName(u"displayLinesExterior_checkBox")
        sizePolicy5.setHeightForWidth(self.displayLinesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLinesExterior_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.displayLinesExterior_checkBox)

        self.displayLines_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.displayLines_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayLines_frame)

        self.displaySurfaces_frame = QFrame(self.display_tab)
        self.displaySurfaces_frame.setObjectName(u"displaySurfaces_frame")
        self.displaySurfaces_frame.setFrameShape(QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displaySurfaces_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName(u"displaySurfaces_checkBox")

        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)

        self.displaySurfacesExterior_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName(u"displaySurfacesExterior_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesExterior_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)

        self.displaySurfacesTranslucent_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName(u"displaySurfacesTranslucent_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesTranslucent_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesTranslucent_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)

        self.displaySurfacesWireframe_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName(u"displaySurfacesWireframe_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesWireframe_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesWireframe_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)

        self.displaySurfaces_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.displaySurfaces_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displaySurfaces_frame)

        self.controls_tabWidget.addTab(self.display_tab, "")
        self.error_statistics_tab = QWidget()
        self.error_statistics_tab.setObjectName(u"error_statistics_tab")
        self.verticalLayout_12 = QVBoxLayout(self.error_statistics_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.error_group_frame = QFrame(self.error_statistics_tab)
        self.error_group_frame.setObjectName(u"error_group_frame")
        self.error_group_frame.setFrameShape(QFrame.StyledPanel)
        self.error_group_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_21 = QFormLayout(self.error_group_frame)
        self.formLayout_21.setObjectName(u"formLayout_21")
        self.formLayout_21.setContentsMargins(0, 0, 0, 0)
        self.displayRMSError_label = QLabel(self.error_group_frame)
        self.displayRMSError_label.setObjectName(u"displayRMSError_label")

        self.formLayout_21.setWidget(0, QFormLayout.LabelRole, self.displayRMSError_label)

        self.displayRMSError_lineEdit = QLineEdit(self.error_group_frame)
        self.displayRMSError_lineEdit.setObjectName(u"displayRMSError_lineEdit")

        self.formLayout_21.setWidget(0, QFormLayout.FieldRole, self.displayRMSError_lineEdit)

        self.displayMaxError_label = QLabel(self.error_group_frame)
        self.displayMaxError_label.setObjectName(u"displayMaxError_label")

        self.formLayout_21.setWidget(1, QFormLayout.LabelRole, self.displayMaxError_label)

        self.displayMaxError_lineEdit = QLineEdit(self.error_group_frame)
        self.displayMaxError_lineEdit.setObjectName(u"displayMaxError_lineEdit")

        self.formLayout_21.setWidget(1, QFormLayout.FieldRole, self.displayMaxError_lineEdit)


        self.verticalLayout_12.addWidget(self.error_group_frame)

        self.controls_tabWidget.addTab(self.error_statistics_tab, "")

        self.verticalLayout.addWidget(self.controls_tabWidget)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.pushButtonDocumentation = QPushButton(self.bottom_frame)
        self.pushButtonDocumentation.setObjectName(u"pushButtonDocumentation")

        self.horizontalLayout_2.addWidget(self.pushButtonDocumentation)

        self.viewAll_pushButton = QPushButton(self.bottom_frame)
        self.viewAll_pushButton.setObjectName(u"viewAll_pushButton")

        self.horizontalLayout_2.addWidget(self.viewAll_pushButton)

        self.stdViews_pushButton = QPushButton(self.bottom_frame)
        self.stdViews_pushButton.setObjectName(u"stdViews_pushButton")

        self.horizontalLayout_2.addWidget(self.stdViews_pushButton)

        self.done_pushButton = QPushButton(self.bottom_frame)
        self.done_pushButton.setObjectName(u"done_pushButton")
        sizePolicy5.setHeightForWidth(self.done_pushButton.sizePolicy().hasHeightForWidth())
        self.done_pushButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.done_pushButton)


        self.verticalLayout.addWidget(self.bottom_frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.alignmentsceneviewerwidget = AlignmentSceneviewerWidget(GeometryFitterWidget)
        self.alignmentsceneviewerwidget.setObjectName(u"alignmentsceneviewerwidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.alignmentsceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.alignmentsceneviewerwidget.setSizePolicy(sizePolicy6)
        self.alignmentsceneviewerwidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.alignmentsceneviewerwidget)


        self.retranslateUi(GeometryFitterWidget)

        self.controls_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GeometryFitterWidget)
    # setupUi

    def retranslateUi(self, GeometryFitterWidget):
        GeometryFitterWidget.setWindowTitle(QCoreApplication.translate("GeometryFitterWidget", u"Geometry Fitter", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("GeometryFitterWidget", u"Control Panel", None))
        self.identifier_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Identifier", None))
        self.steps_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Steps:", None))
        self.stepsAddAlign_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Add Align", None))
        self.stepsAddConfig_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Add Config", None))
        self.stepsAddFit_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Add Fit", None))
        self.stepsDelete_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Delete", None))
        self.configInitial_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Initial", None))
        self.configModelCoordinates_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Model coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configModelCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Model coordinate field to fit.<br/>Output fitted field takes name of this field preceded by &quot;fitted &quot;.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configModelFitGrouplabel.setText(QCoreApplication.translate("GeometryFitterWidget", u"Model fit group:", None))
#if QT_CONFIG(tooltip)
        self.configModelFitGroup_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Optional subset of model to fit.<br/>If not set, whole model is fitted.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.configFlattenGroup_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Optional surface or line group to constrain to z = 0.</p><p>Data weight for this group scales flattening term.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configFlattenGroup_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Flatten group:", None))
        self.configFibreOrientation_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Fibre orientation:", None))
#if QT_CONFIG(tooltip)
        self.configFibreOrientation_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Optional field supplying Euler angles to rotate local 'fibre' axes on which strain and curvature penalties are applied. Clear to apply on global x, y, z axes.</p><p>Required for applying strain and curvature penalties on 2D mesh fits with 3 coordinate components.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDataCoordinates_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configDataCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Field giving coordinates of data points.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Diagnostic level:", None))
        self.configMarkerGroup_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker group:", None))
#if QT_CONFIG(tooltip)
        self.configDiagnosticLevel_spinBox.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Increase to 1 to see diagnostic output, 2 to see more verbose optimization diagnostic output.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.config_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Config", None))
        self.align_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Align", None))
        self.alignGroups_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Align groups", None))
        self.alignMarkers_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Align markers", None))
        self.alignRotation_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Rotation:", None))
        self.alignScale_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Scale:", None))
        self.alignTranslation_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Translation:", None))
        self.fit_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Fit", None))
        self.fitIterations_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Iterations:", None))
#if QT_CONFIG(tooltip)
        self.fitIterations_spinBox.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Number of full iterations with reprojection of data.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fitMaximumSubIterations_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Maximum subiterations:", None))
#if QT_CONFIG(tooltip)
        self.fitUpdateReferenceState_checkBox.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Advanced: Update reference state to coordinates at end of this step for applying subsequent strain and curvature penalties.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fitUpdateReferenceState_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Update reference state", None))
        self.groupSettings_groupBox.setTitle(QCoreApplication.translate("GeometryFitterWidget", u"Group settings", None))
        self.groupSettings_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Group:", None))
        self.groupConfigCentralProjection_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Central Projection", None))
        self.groupConfigSetCentralProjection_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Set", None))
        self.groupConfigDataProportion_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data Proportion", None))
#if QT_CONFIG(tooltip)
        self.groupConfigDataProportion_lineEdit.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"Value from 0.0 to 1.0", None))
#endif // QT_CONFIG(tooltip)
        self.groupFitDataWeight_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data Weight", None))
        self.groupFitStrainPenalty_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Strain Penalty", None))
        self.groupFitCurvaturePenalty_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Curvature Penalty", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Axes", None))
        self.displayGroup_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Group:", None))
#if QT_CONFIG(tooltip)
        self.displayGroup_fieldChooser.setToolTip(QCoreApplication.translate("GeometryFitterWidget", u"<html><head/><body><p>Optional group to limit display of model and data to.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayMarkerDataNames_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker data names", None))
        self.displayMarkerDataPoints_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker data points", None))
        self.displayMarkerNames_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker names", None))
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker points", None))
        self.displayMarkerDataProjections_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Marker projections", None))
        self.displayDataPoints_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data points", None))
        self.displayDataProjections_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data projections", None))
        self.displayDataProjectionPoints_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Data projection points", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Node numbers", None))
        self.displayNodeDerivatives_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Node derivatives", None))
        self.displayNodeDerivativeLabelsD1_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D1", None))
        self.displayNodeDerivativeLabelsD2_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D2", None))
        self.displayNodeDerivativeLabelsD3_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D3", None))
        self.displayNodeDerivativeLabelsD12_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D12", None))
        self.displayNodeDerivativeLabelsD13_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D13", None))
        self.displayNodeDerivativeLabelsD23_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D23", None))
        self.displayNodeDerivativeLabelsD123_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"D123", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Element axes", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Exterior", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("GeometryFitterWidget", u"Wireframe", None))
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.display_tab), QCoreApplication.translate("GeometryFitterWidget", u"Display", None))
        self.displayRMSError_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"RMS error:", None))
        self.displayMaxError_label.setText(QCoreApplication.translate("GeometryFitterWidget", u"Maximum error:", None))
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.error_statistics_tab), QCoreApplication.translate("GeometryFitterWidget", u"Error Statistics", None))
        self.pushButtonDocumentation.setText(QCoreApplication.translate("GeometryFitterWidget", u"Online Documentation", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"View All", None))
        self.stdViews_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Std. Views", None))
        self.done_pushButton.setText(QCoreApplication.translate("GeometryFitterWidget", u"Done", None))
    # retranslateUi

