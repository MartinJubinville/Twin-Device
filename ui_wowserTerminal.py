# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wowserTerminal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QToolBar, QWidget)

class Ui_wowserTerminal(object):
    def setupUi(self, wowserTerminal):
        if not wowserTerminal.objectName():
            wowserTerminal.setObjectName(u"wowserTerminal")
        wowserTerminal.resize(684, 536)
        self.actionConnect = QAction(wowserTerminal)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(wowserTerminal)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.actionReport = QAction(wowserTerminal)
        self.actionReport.setObjectName(u"actionReport")
        self.actionFormat = QAction(wowserTerminal)
        self.actionFormat.setObjectName(u"actionFormat")
        self.actionWowSerSettings = QAction(wowserTerminal)
        self.actionWowSerSettings.setObjectName(u"actionWowSerSettings")
        icon = QIcon()
        icon.addFile(u"stuffserial/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWowSerSettings.setIcon(icon)
        self.actionWowSerSettings.setMenuRole(QAction.NoRole)
        self.actionWowSerConnect = QAction(wowserTerminal)
        self.actionWowSerConnect.setObjectName(u"actionWowSerConnect")
        icon1 = QIcon()
        icon1.addFile(u"stuffserial/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWowSerConnect.setIcon(icon1)
        self.actionWowSerConnect.setMenuRole(QAction.NoRole)
        self.actionWowSerDisconnect = QAction(wowserTerminal)
        self.actionWowSerDisconnect.setObjectName(u"actionWowSerDisconnect")
        icon2 = QIcon()
        icon2.addFile(u"stuffserial/disconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWowSerDisconnect.setIcon(icon2)
        self.actionWowSerDisconnect.setMenuRole(QAction.NoRole)
        self.actionWowSerTerminalWipe = QAction(wowserTerminal)
        self.actionWowSerTerminalWipe.setObjectName(u"actionWowSerTerminalWipe")
        icon3 = QIcon()
        icon3.addFile(u"stuffserial/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWowSerTerminalWipe.setIcon(icon3)
        self.actionWowSerTerminalWipe.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(wowserTerminal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_TerminalUserCommandLine = QLineEdit(self.centralwidget)
        self.lineEdit_TerminalUserCommandLine.setObjectName(u"lineEdit_TerminalUserCommandLine")
        self.lineEdit_TerminalUserCommandLine.setGeometry(QRect(40, 70, 631, 21))
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.lineEdit_TerminalUserCommandLine.setFont(font)
        self.pushButton_Done = QPushButton(self.centralwidget)
        self.pushButton_Done.setObjectName(u"pushButton_Done")
        self.pushButton_Done.setGeometry(QRect(570, 400, 100, 32))
        self.pushButton_Done.setCheckable(False)
        self.pushButton_Done.setAutoDefault(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 101, 16))
        self.textBrowser_TerminalScreen = QTextBrowser(self.centralwidget)
        self.textBrowser_TerminalScreen.setObjectName(u"textBrowser_TerminalScreen")
        self.textBrowser_TerminalScreen.setGeometry(QRect(40, 110, 631, 181))
        self.textBrowser_TerminalScreen.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 310, 161, 16))
        wowserTerminal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wowserTerminal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 684, 24))
        self.menuSerial = QMenu(self.menubar)
        self.menuSerial.setObjectName(u"menuSerial")
        wowserTerminal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wowserTerminal)
        self.statusbar.setObjectName(u"statusbar")
        wowserTerminal.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(wowserTerminal)
        self.toolBar.setObjectName(u"toolBar")
        wowserTerminal.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuSerial.menuAction())
        self.menuSerial.addAction(self.actionConnect)
        self.menuSerial.addAction(self.actionDisconnect)
        self.menuSerial.addSeparator()
        self.menuSerial.addAction(self.actionReport)
        self.menuSerial.addAction(self.actionFormat)
        self.menuSerial.addSeparator()
        self.menuSerial.addAction(self.actionWowSerConnect)
        self.menuSerial.addAction(self.actionWowSerDisconnect)
        self.menuSerial.addAction(self.actionWowSerSettings)
        self.menuSerial.addAction(self.actionWowSerTerminalWipe)
        self.toolBar.addAction(self.actionWowSerConnect)
        self.toolBar.addAction(self.actionWowSerDisconnect)
        self.toolBar.addAction(self.actionWowSerSettings)
        self.toolBar.addAction(self.actionWowSerTerminalWipe)

        self.retranslateUi(wowserTerminal)

        self.pushButton_Done.setDefault(True)


        QMetaObject.connectSlotsByName(wowserTerminal)
    # setupUi

    def retranslateUi(self, wowserTerminal):
        wowserTerminal.setWindowTitle(QCoreApplication.translate("wowserTerminal", u"WowSer Terminal", None))
        self.actionConnect.setText(QCoreApplication.translate("wowserTerminal", u"Connect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("wowserTerminal", u"Disconnect", None))
        self.actionReport.setText(QCoreApplication.translate("wowserTerminal", u"Report", None))
        self.actionFormat.setText(QCoreApplication.translate("wowserTerminal", u"Format", None))
        self.actionWowSerSettings.setText(QCoreApplication.translate("wowserTerminal", u"WowSerSettings", None))
#if QT_CONFIG(tooltip)
        self.actionWowSerSettings.setToolTip(QCoreApplication.translate("wowserTerminal", u"Serial port settings configuration...", None))
#endif // QT_CONFIG(tooltip)
        self.actionWowSerConnect.setText(QCoreApplication.translate("wowserTerminal", u"WowSerConnect", None))
#if QT_CONFIG(tooltip)
        self.actionWowSerConnect.setToolTip(QCoreApplication.translate("wowserTerminal", u"Connect with the serial port...", None))
#endif // QT_CONFIG(tooltip)
        self.actionWowSerDisconnect.setText(QCoreApplication.translate("wowserTerminal", u"WowSerDisconnect", None))
#if QT_CONFIG(tooltip)
        self.actionWowSerDisconnect.setToolTip(QCoreApplication.translate("wowserTerminal", u"Disconnect the serial port...", None))
#endif // QT_CONFIG(tooltip)
        self.actionWowSerTerminalWipe.setText(QCoreApplication.translate("wowserTerminal", u"WowSerTerminalWipe", None))
#if QT_CONFIG(tooltip)
        self.actionWowSerTerminalWipe.setToolTip(QCoreApplication.translate("wowserTerminal", u"Clear the serial port terminal...", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Done.setText(QCoreApplication.translate("wowserTerminal", u"Done", None))
        self.label.setText(QCoreApplication.translate("wowserTerminal", u"<html><head/><body><p><span style=\" font-weight:700;\">Terminal</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("wowserTerminal", u"<html><head/><body><p><span style=\" font-weight:700;\">Customized Commands </span></p></body></html>", None))
        self.menuSerial.setTitle(QCoreApplication.translate("wowserTerminal", u"Serial", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("wowserTerminal", u"toolBar", None))
    # retranslateUi

