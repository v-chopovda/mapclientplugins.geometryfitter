# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometricfitwidget.ui'
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


class Ui_GeometricFitWidget(object):
    def setupUi(self, GeometricFitWidget):
        if not GeometricFitWidget.objectName():
            GeometricFitWidget.setObjectName(u"GeometricFitWidget")
        GeometricFitWidget.resize(1718, 1101)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeometricFitWidget.sizePolicy().hasHeightForWidth())
        GeometricFitWidget.setSizePolicy(sizePolicy)
        GeometricFitWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(GeometricFitWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(GeometricFitWidget)
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

        self.steps_listView = QListView(self.steps_groupBox)
        self.steps_listView.setObjectName(u"steps_listView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.steps_listView.sizePolicy().hasHeightForWidth())
        self.steps_listView.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.steps_listView)

        self.stepedit_scrollArea = QScrollArea(self.steps_groupBox)
        self.stepedit_scrollArea.setObjectName(u"stepedit_scrollArea")
        sizePolicy.setHeightForWidth(self.stepedit_scrollArea.sizePolicy().hasHeightForWidth())
        self.stepedit_scrollArea.setSizePolicy(sizePolicy)
        self.stepedit_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stepedit_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.stepedit_scrollArea.setWidgetResizable(True)
        self.stepedit_scrollAreaWidgetContents = QWidget()
        self.stepedit_scrollAreaWidgetContents.setObjectName(u"stepedit_scrollAreaWidgetContents")
        self.stepedit_scrollAreaWidgetContents.setGeometry(QRect(0, -238, 352, 585))
        self.verticalLayout_3 = QVBoxLayout(self.stepedit_scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.config_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.config_groupBox.setObjectName(u"config_groupBox")
        sizePolicy.setHeightForWidth(self.config_groupBox.sizePolicy().hasHeightForWidth())
        self.config_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.config_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.configInitial_groupBox = QGroupBox(self.config_groupBox)
        self.configInitial_groupBox.setObjectName(u"configInitial_groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.configInitial_groupBox.sizePolicy().hasHeightForWidth())
        self.configInitial_groupBox.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.configInitial_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.configModelCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configModelCoordinates_label.setObjectName(u"configModelCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configModelCoordinates_label)

        self.configModelCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configModelCoordinates_fieldChooser.setObjectName(u"configModelCoordinates_fieldChooser")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.configModelCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configModelCoordinates_fieldChooser.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configModelCoordinates_fieldChooser)

        self.configDataCoordinates_label = QLabel(self.configInitial_groupBox)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy4.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)

        self.configDiagnosticLevel_spinBox = QSpinBox(self.configInitial_groupBox)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)

        self.configDiagnosticLevel_label = QLabel(self.configInitial_groupBox)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configMarkerGroup_label = QLabel(self.configInitial_groupBox)
        self.configMarkerGroup_label.setObjectName(u"configMarkerGroup_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configMarkerGroup_label)

        self.configMarkerGroup_fieldChooser = FieldChooserWidget(self.configInitial_groupBox)
        self.configMarkerGroup_fieldChooser.setObjectName(u"configMarkerGroup_fieldChooser")
        sizePolicy4.setHeightForWidth(self.configMarkerGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configMarkerGroup_fieldChooser.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configMarkerGroup_fieldChooser)


        self.verticalLayout_4.addWidget(self.configInitial_groupBox)

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
        sizePolicy4.setHeightForWidth(self.alignRotation_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignRotation_lineEdit.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.alignRotation_lineEdit)

        self.alignScale_label = QLabel(self.align_groupBox)
        self.alignScale_label.setObjectName(u"alignScale_label")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.alignScale_label)

        self.alignScale_lineEdit = QLineEdit(self.align_groupBox)
        self.alignScale_lineEdit.setObjectName(u"alignScale_lineEdit")
        sizePolicy4.setHeightForWidth(self.alignScale_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignScale_lineEdit.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.alignScale_lineEdit)

        self.alignTranslation_label = QLabel(self.align_groupBox)
        self.alignTranslation_label.setObjectName(u"alignTranslation_label")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.alignTranslation_label)

        self.alignTranslation_lineEdit = QLineEdit(self.align_groupBox)
        self.alignTranslation_lineEdit.setObjectName(u"alignTranslation_lineEdit")
        sizePolicy4.setHeightForWidth(self.alignTranslation_lineEdit.sizePolicy().hasHeightForWidth())
        self.alignTranslation_lineEdit.setSizePolicy(sizePolicy4)

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
        sizePolicy4.setHeightForWidth(self.fitIterations_spinBox.sizePolicy().hasHeightForWidth())
        self.fitIterations_spinBox.setSizePolicy(sizePolicy4)
        self.fitIterations_spinBox.setMinimum(1)
        self.fitIterations_spinBox.setMaximum(1000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.fitIterations_spinBox)

        self.fitMaximumSubIterations_label = QLabel(self.fit_groupBox)
        self.fitMaximumSubIterations_label.setObjectName(u"fitMaximumSubIterations_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.fitMaximumSubIterations_label)

        self.fitMaximumSubIterations_spinBox = QSpinBox(self.fit_groupBox)
        self.fitMaximumSubIterations_spinBox.setObjectName(u"fitMaximumSubIterations_spinBox")
        sizePolicy4.setHeightForWidth(self.fitMaximumSubIterations_spinBox.sizePolicy().hasHeightForWidth())
        self.fitMaximumSubIterations_spinBox.setSizePolicy(sizePolicy4)
        self.fitMaximumSubIterations_spinBox.setMinimum(1)
        self.fitMaximumSubIterations_spinBox.setMaximum(1000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.fitMaximumSubIterations_spinBox)

        self.fitUpdateReferenceState_checkBox = QCheckBox(self.fit_groupBox)
        self.fitUpdateReferenceState_checkBox.setObjectName(u"fitUpdateReferenceState_checkBox")
        sizePolicy.setHeightForWidth(self.fitUpdateReferenceState_checkBox.sizePolicy().hasHeightForWidth())
        self.fitUpdateReferenceState_checkBox.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.fitUpdateReferenceState_checkBox)


        self.verticalLayout_3.addWidget(self.fit_groupBox)

        self.groupSetting_groupBox = QGroupBox(self.stepedit_scrollAreaWidgetContents)
        self.groupSetting_groupBox.setObjectName(u"groupSetting_groupBox")
        sizePolicy3.setHeightForWidth(self.groupSetting_groupBox.sizePolicy().hasHeightForWidth())
        self.groupSetting_groupBox.setSizePolicy(sizePolicy3)
        self.configSettingGroup_Layout = QFormLayout(self.groupSetting_groupBox)
        self.configSettingGroup_Layout.setObjectName(u"configSettingGroup_Layout")
        self.configSettingGroup_Layout.setContentsMargins(-1, -1, -1, 0)
        self.configSettingGroup_label = QLabel(self.groupSetting_groupBox)
        self.configSettingGroup_label.setObjectName(u"configSettingGroup_label")

        self.configSettingGroup_Layout.setWidget(1, QFormLayout.LabelRole, self.configSettingGroup_label)

        self.configSettingGroup_fieldChooser = FieldChooserWidget(self.groupSetting_groupBox)
        self.configSettingGroup_fieldChooser.setObjectName(u"configSettingGroup_fieldChooser")
        sizePolicy4.setHeightForWidth(self.configSettingGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configSettingGroup_fieldChooser.setSizePolicy(sizePolicy4)

        self.configSettingGroup_Layout.setWidget(1, QFormLayout.FieldRole, self.configSettingGroup_fieldChooser)

        self.configCentralProjection_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configCentralProjection_checkBox.setObjectName(u"configCentralProjection_checkBox")

        self.configSettingGroup_Layout.setWidget(2, QFormLayout.LabelRole, self.configCentralProjection_checkBox)

        self.configSetCentralProjection_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configSetCentralProjection_checkBox.setObjectName(u"configSetCentralProjection_checkBox")

        self.configSettingGroup_Layout.setWidget(2, QFormLayout.FieldRole, self.configSetCentralProjection_checkBox)

        self.configDataProportion_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configDataProportion_checkBox.setObjectName(u"configDataProportion_checkBox")

        self.configSettingGroup_Layout.setWidget(3, QFormLayout.LabelRole, self.configDataProportion_checkBox)

        self.configDataProportion_lineEdit = QLineEdit(self.groupSetting_groupBox)
        self.configDataProportion_lineEdit.setObjectName(u"configDataProportion_lineEdit")

        self.configSettingGroup_Layout.setWidget(3, QFormLayout.FieldRole, self.configDataProportion_lineEdit)

        self.configDataWeight_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configDataWeight_checkBox.setObjectName(u"configDataWeight_checkBox")

        self.configSettingGroup_Layout.setWidget(4, QFormLayout.LabelRole, self.configDataWeight_checkBox)

        self.configDataWeight_lineEdit = QLineEdit(self.groupSetting_groupBox)
        self.configDataWeight_lineEdit.setObjectName(u"configDataWeight_lineEdit")

        self.configSettingGroup_Layout.setWidget(4, QFormLayout.FieldRole, self.configDataWeight_lineEdit)

        self.configStrainPenalty_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configStrainPenalty_checkBox.setObjectName(u"configStrainPenalty_checkBox")

        self.configSettingGroup_Layout.setWidget(5, QFormLayout.LabelRole, self.configStrainPenalty_checkBox)

        self.configStrainPenalty_lineEdit = QLineEdit(self.groupSetting_groupBox)
        self.configStrainPenalty_lineEdit.setObjectName(u"configStrainPenalty_lineEdit")

        self.configSettingGroup_Layout.setWidget(5, QFormLayout.FieldRole, self.configStrainPenalty_lineEdit)

        self.configCurvaturePenalty_checkBox = QCheckBox(self.groupSetting_groupBox)
        self.configCurvaturePenalty_checkBox.setObjectName(u"configCurvaturePenalty_checkBox")

        self.configSettingGroup_Layout.setWidget(6, QFormLayout.LabelRole, self.configCurvaturePenalty_checkBox)

        self.configCurvaturePenalty_lineEdit = QLineEdit(self.groupSetting_groupBox)
        self.configCurvaturePenalty_lineEdit.setObjectName(u"configCurvaturePenalty_lineEdit")

        self.configSettingGroup_Layout.setWidget(6, QFormLayout.FieldRole, self.configCurvaturePenalty_lineEdit)


        self.verticalLayout_3.addWidget(self.groupSetting_groupBox)

        self.stepedit_scrollArea.setWidget(self.stepedit_scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.stepedit_scrollArea)


        self.verticalLayout.addWidget(self.steps_groupBox)

        self.display_groupBox = QGroupBox(self.dockWidgetContents)
        self.display_groupBox.setObjectName(u"display_groupBox")
        sizePolicy.setHeightForWidth(self.display_groupBox.sizePolicy().hasHeightForWidth())
        self.display_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.display_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_groupBox)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displaytMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.displaytMisc_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayMarker_frame = QFrame(self.display_groupBox)
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

        self.displayData_frame = QFrame(self.display_groupBox)
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

        self.displayNodes_frame = QFrame(self.display_groupBox)
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

        self.displayNodeDerivativeLabels_frame = QFrame(self.display_groupBox)
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

        self.displayElements_frame = QFrame(self.display_groupBox)
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

        self.displayLines_frame = QFrame(self.display_groupBox)
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

        self.displaySurfaces_frame = QFrame(self.display_groupBox)
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


        self.verticalLayout.addWidget(self.display_groupBox)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
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

        self.alignmentsceneviewerwidget = AlignmentSceneviewerWidget(GeometricFitWidget)
        self.alignmentsceneviewerwidget.setObjectName(u"alignmentsceneviewerwidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.alignmentsceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.alignmentsceneviewerwidget.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.alignmentsceneviewerwidget)


        self.retranslateUi(GeometricFitWidget)

        QMetaObject.connectSlotsByName(GeometricFitWidget)
    # setupUi

    def retranslateUi(self, GeometricFitWidget):
        GeometricFitWidget.setWindowTitle(QCoreApplication.translate("GeometricFitWidget", u"Geometric Fit", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("GeometricFitWidget", u"Control Panel", None))
        self.identifier_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Identifier", None))
        self.steps_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Steps:", None))
        self.stepsAddAlign_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Add Align", None))
        self.stepsAddConfig_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Add Config", None))
        self.stepsAddFit_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Add Fit", None))
        self.stepsDelete_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Delete", None))
        self.config_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Config", None))
        self.configInitial_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Initial", None))
        self.configModelCoordinates_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Model coordinates:", None))
        self.configDataCoordinates_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Data coordinates:", None))
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Diagnostic level:", None))
        self.configMarkerGroup_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker group:", None))
        self.align_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Align", None))
        self.alignGroups_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Align groups", None))
        self.alignMarkers_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Align markers", None))
        self.alignRotation_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Rotation:", None))
        self.alignScale_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Scale:", None))
        self.alignTranslation_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Translation:", None))
        self.fit_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Fit", None))
        self.fitIterations_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Iterations:", None))
        self.fitMaximumSubIterations_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Maximum subiterations:", None))
        self.fitUpdateReferenceState_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Update reference state", None))
        self.groupSetting_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Group settings", None))
        self.configSettingGroup_label.setText(QCoreApplication.translate("GeometricFitWidget", u"Group:", None))
        self.configCentralProjection_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Central Projection", None))
        self.configSetCentralProjection_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Set", None))
        self.configDataProportion_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Data Proportion", None))
#if QT_CONFIG(tooltip)
        self.configDataProportion_lineEdit.setToolTip(QCoreApplication.translate("GeometricFitWidget", u"Value from 0.0 to 1.0", None))
#endif // QT_CONFIG(tooltip)
        self.configDataWeight_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Data Weight", None))
        self.configStrainPenalty_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Strain Penalty", None))
        self.configCurvaturePenalty_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Curvature Penalty", None))
        self.display_groupBox.setTitle(QCoreApplication.translate("GeometricFitWidget", u"Display:", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Axes", None))
        self.displayMarkerDataNames_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker data names", None))
        self.displayMarkerDataPoints_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker data points", None))
        self.displayMarkerNames_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker names", None))
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker points", None))
        self.displayMarkerDataProjections_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Marker projections", None))
        self.displayDataPoints_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Data points", None))
        self.displayDataProjections_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Data projections", None))
        self.displayDataProjectionPoints_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Data projection points", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Node numbers", None))
        self.displayNodeDerivatives_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Node derivatives", None))
        self.displayNodeDerivativeLabelsD1_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D1", None))
        self.displayNodeDerivativeLabelsD2_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D2", None))
        self.displayNodeDerivativeLabelsD3_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D3", None))
        self.displayNodeDerivativeLabelsD12_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D12", None))
        self.displayNodeDerivativeLabelsD13_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D13", None))
        self.displayNodeDerivativeLabelsD23_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D23", None))
        self.displayNodeDerivativeLabelsD123_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"D123", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Element axes", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Exterior", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("GeometricFitWidget", u"Wireframe", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"View All", None))
        self.stdViews_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Std. Views", None))
        self.done_pushButton.setText(QCoreApplication.translate("GeometricFitWidget", u"Done", None))
    # retranslateUi

