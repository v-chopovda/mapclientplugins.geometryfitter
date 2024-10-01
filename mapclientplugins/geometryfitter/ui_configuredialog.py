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
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

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
        self.labelIdentifier = QLabel(self.configGroupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")
        self.labelIdentifier.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelIdentifier, 0, 0, 1, 1)

        self.labelRunFitHeadless = QLabel(self.configGroupBox)
        self.labelRunFitHeadless.setObjectName(u"labelRunFitHeadless")
        self.labelRunFitHeadless.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelRunFitHeadless, 2, 0, 1, 1)

        self.checkBoxResetSettings = QCheckBox(self.configGroupBox)
        self.checkBoxResetSettings.setObjectName(u"checkBoxResetSettings")

        self.gridLayout_2.addWidget(self.checkBoxResetSettings, 1, 2, 1, 1)

        self.labelResetSettings = QLabel(self.configGroupBox)
        self.labelResetSettings.setObjectName(u"labelResetSettings")
        self.labelResetSettings.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelResetSettings, 1, 0, 1, 1)

        self.checkBoxRunFitHeadless = QCheckBox(self.configGroupBox)
        self.checkBoxRunFitHeadless.setObjectName(u"checkBoxRunFitHeadless")

        self.gridLayout_2.addWidget(self.checkBoxRunFitHeadless, 2, 2, 1, 1)

        self.lineEditIdentifier = QLineEdit(self.configGroupBox)
        self.lineEditIdentifier.setObjectName(u"lineEditIdentifier")

        self.gridLayout_2.addWidget(self.lineEditIdentifier, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.configGroupBox, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Geometry Fitter", None))
        self.configGroupBox.setTitle("")
        self.labelIdentifier.setText(QCoreApplication.translate("ConfigureDialog", u"Identifier:", None))
#if QT_CONFIG(tooltip)
        self.labelRunFitHeadless.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Reset the settings to their default values on the next run", None))
#endif // QT_CONFIG(tooltip)
        self.labelRunFitHeadless.setText(QCoreApplication.translate("ConfigureDialog", u"Run fit headless:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxResetSettings.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Reset the settings to their default values on the next run", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxResetSettings.setText("")
#if QT_CONFIG(tooltip)
        self.labelResetSettings.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Reset the settings to their default values on the next run", None))
#endif // QT_CONFIG(tooltip)
        self.labelResetSettings.setText(QCoreApplication.translate("ConfigureDialog", u"Reset settings:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxRunFitHeadless.setToolTip(QCoreApplication.translate("ConfigureDialog", u"Run the fit as it is currently defined without showing the user interface.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxRunFitHeadless.setText("")
    # retranslateUi

