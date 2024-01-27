# Copyright (C) 2024 Wild Rose Technologies Inc.

from PySide6.QtCore import Qt, Signal, Slot, QPoint
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit

from ui_wowserTerminal import Ui_wowserTerminal
# from ui_wowserSettings import Ui_SettingsDialog  
from wowserSettings import wowserSettingsDialog


class wowserTerminal(QMainWindow):
    # Signals 
    wowserState = Signal(str)               # Tell main app we are on
    

    # Methods
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_ui = Ui_wowserTerminal()
        self.m_ui.setupUi(self)

        self.move(QPoint(20, 20))
        # *** Let's try to format the windows for green on black
        # *** Designer crashes in trying to do this, so we will code it
        #self.m_ui.

        # Let's try to instantiate WowSerSettings here
        # It will be hierachical and more easier to bring in to other projects
        self.myWowSerSettingsDialogue = wowserSettingsDialog()
        self.myWowSerSettingsDialogue.show()


        #connections
        self.m_ui.actionWowSerSettings.triggered.connect(self.woswerSettingsWindowShow) ### <----
        self.myWowSerSettingsDialogue.m_ui.applyButton.clicked.connect(self.wowserSerialSettingsUpdated)
        


    #Slots
    @Slot()
    def wowserRequestReceived(self):   #Note: the pass of "self"
        print("wowserRequest handled by wowser")
        self.move(QPoint(50,50))
        self.show()
        self.setFocus()
        self.wowserState.emit("Heya!")
        self.raise_()
        self.activateWindow()

    @Slot()
    def woswerSettingsWindowShow(self):
        print("Someone wants the WowSer Serial Settings dialog")
        self.myWowSerSettingsDialogue.raise_()
        #self.myWowerSettingsDialogue.show()
        self.myWowSerSettingsDialogue.activateWindow()

    @Slot()
    def wowserSerialSettingsUpdated(self):
        print("WowSer serial settings were changed")
        self.raise_()
    
        


