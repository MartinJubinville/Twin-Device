# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogsecondwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QPlainTextEdit, QSizePolicy, QWidget)

class Ui_DialogSecondWindow(object):
    def setupUi(self, DialogSecondWindow):
        if not DialogSecondWindow.objectName():
            DialogSecondWindow.setObjectName(u"DialogSecondWindow")
        DialogSecondWindow.resize(640, 480)
        self.buttonBox = QDialogButtonBox(DialogSecondWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.plainTextEdit = QPlainTextEdit(DialogSecondWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 20, 401, 151))

        self.retranslateUi(DialogSecondWindow)
        self.buttonBox.accepted.connect(DialogSecondWindow.accept)
        self.buttonBox.rejected.connect(DialogSecondWindow.reject)

        QMetaObject.connectSlotsByName(DialogSecondWindow)
    # setupUi

    def retranslateUi(self, DialogSecondWindow):
        DialogSecondWindow.setWindowTitle(QCoreApplication.translate("DialogSecondWindow", u"Dialog", None))
    # retranslateUi

