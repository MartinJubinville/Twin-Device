# Copyright (C) 2024 Wild Rose Technologies Inc.

from PySide6.QtWidgets import QMainWindow

from PySide6.QtCore import QIODevice, Signal, Slot     # both of these idea came from serial demo
# I don't know why this Slot is imported, but is it used below
from PySide6.QtCore import QPoint               # to move window to certain point position

from ui_mainwindow import Ui_MainWindow
from ui_wowserSettings import Ui_SettingsDialog
#from ui_dialogsecondwindow import Ui_DialogSecondWindow


from dialogsecondwindow import DialogSecondWindow # bringing it all into this one
from wowser import wowserTerminal


class TwinDeviceMainWindow(QMainWindow):

    # Signals 
    wowserRequest = Signal(str)

    def __init__(self):
        super(TwinDeviceMainWindow, self).__init__()
        self.ui = Ui_MainWindow()                           # write in the ui
        self.ui.setupUi(self)

        self.myDialogSecondWindow = DialogSecondWindow()  # Note the lack of ".ui"
        #self.wowserRequest.connect(self.wowserRequestInTheAir)

        self.myWowserTerminal = wowserTerminal()
        self.myWowserTerminal.show()
        self.myWowserTerminal.hide()
        self.myWowserTerminal.raise_()
        self.myWowserTerminal.activateWindow()
        
        self.wowserRequest.connect(self.myWowserTerminal.wowserRequestReceived)
        self.myWowserTerminal.wowserState.connect(self.wowserStateChanged)
        self.myWowserTerminal.m_ui.pushButton_Done.clicked.connect(self.wowserTerminalExited)

        self.ui.actionReport.triggered.connect(self.serialReportConfigure)
        self.ui.actionDisconnect.triggered.connect(self.announceEventHappened)
        self.ui.actionDisconnect.triggered.connect(self.serialDisconnectHappened)
        self.ui.actionDisconnect.triggered.connect(self.announceEventHappened)

    @Slot()
    def serialReportConfigure(self):
        print("Serial Report / Configure was Sellected")
        self.wowserRequest.emit("WowSerTerminal")
        print("Emitted wowserRequest")
        #self.hide()
        #self.myDialogSecondWindow.show()
    
    @Slot()
    def wowserStateChanged(self):
        self.show()
        #self.m_ui.label
        self.ui.labelWowSerState.setText("WowSer changed")
        print("aksdfjasdfjdj")

    @Slot()
    def serialDisconnectHappened(self):
        print("Serial Disconnect was Sellected")
        
    @Slot() 
    def announceEventHappened(self):
        print("Event Happened")
        self.myDialogSecondWindow.move(QPoint(20, 20))

    @Slot(str)
    def wowserRequestInTheAir(self):
        print("mainwindow received it's own wowser request")

    @Slot(str)
    def wowserTerminalExited(self):
        print("WowSerTerminal exited")
        self.activateWindow()
        self.raise_()
