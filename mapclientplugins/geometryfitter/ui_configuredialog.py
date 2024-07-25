# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.gridLayout_2 = QGridLayout(self.configGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.gridLayout_2.addWidget(self.lineEdit0, 0, 1, 1, 1)

        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")
        self.label0.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)

        self.labelResetSettings = QLabel(self.configGroupBox)
        self.labelResetSettings.setObjectName(u"labelResetSettings")
        self.labelResetSettings.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelResetSettings, 1, 0, 1, 1)

        self.checkBoxResetSettings = QCheckBox(self.configGroupBox)
        self.checkBoxResetSettings.setObjectName(u"checkBoxResetSettings")

        self.gridLayout_2.addWidget(self.checkBoxResetSettings, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Geometry Fitter", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:", None))
#if QT_CONFIG(tooltip)
        self.labelResetSettings.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Reset the settings to their default values on the next run", None))
#endif // QT_CONFIG(tooltip)
        self.labelResetSettings.setText(QCoreApplication.translate("ConfigureDialog", u"Reset settings:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxResetSettings.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Reset the settings to their default values on the next run", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxResetSettings.setText("")
    # retranslateUi

