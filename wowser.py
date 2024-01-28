# Copyright (C) 2024 Wild Rose Technologies Inc.
# Note: This program part is called WowSer, but uses Ui_wowserTerminal
#     since it is like a terminal that can come up when requested.

from PySide6.QtCore import Qt, Signal, Slot, QPoint
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit
from PySide6.QtGui import QPalette

from ui_wowserTerminal import Ui_wowserTerminal
from wowserSettings import wowserSettingsDialog # replace SettingsDialog in Sample

# *** From sample
from PySide6.QtCore import QIODeviceBase, Slot 
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox
from PySide6.QtSerialPort import QSerialPort


# *** From sample
HELP = """The <b>WowSer Terminal<b> to add funtionality to PySide6 creations."""

# *** From sample
# *** This function will print a string at the bottom of the window
def description(s):
    return(f"Connected to {s.name} : {s.string_baud_rate}, "
           f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
           f"{s.string_flow_control}")
class wowserTerminal(QMainWindow):
    # Signals 
    wowserState = Signal(str)               # Tell main app we are on
    

    # Methods
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_ui = Ui_wowserTerminal()                     # Ui_MainWindow() in Sample
        self.m_status = QLabel()                            # from Sample
        ### self.m_console = Console()  # in Sample this is a QPlainTextEdit()
        ### self.m_settings = SettingsDialog(self)  # in Sample, but replaced by myWowSerSettingsDialog below
        self.m_serial = QSerialPort(self)

        self.m_ui.setupUi(self)

        ### self.m_console.setEnabled(False)                    # from Sample
        

        self.move(QPoint(20, 20))
        # *** Let's try to format the windows for green on black
        # *** Designer crashes in trying to do this, so we will code it
        self.myPalette = self.palette()
        self.myPalette.setColor(QPalette.Base, Qt.black)
        self.myPalette.setColor(QPalette.Text, Qt.green)
        self.setPalette(self.myPalette)


        # Let's try to instantiate WowSerSettings here
        # It will be hierachical and more easier to bring in to other projects
        self.myWowSerSettingsDialogue = wowserSettingsDialog()
        self.myWowSerSettingsDialogue.show()


        #connections
        self.m_ui.actionWowSerSettings.triggered.connect(self.woswerSettingsWindowShow) ### <----
        self.myWowSerSettingsDialogue.m_ui.applyButton.clicked.connect(self.wowserSerialSettingsUpdated)
        #self.m_ui.lineEdit_TerminalUserCommandLine.textChanged.connect(self.echoTerminalText) #need more
        self.m_ui.lineEdit_TerminalUserCommandLine.returnPressed.connect(self.echoTerminalText)

        


    #Slots
        
    @Slot()
    def echoTerminalText(self):
        print("Text was entered in the Terminal")
        self.m_ui.textBrowser_TerminalScreen.append(self.m_ui.lineEdit_TerminalUserCommandLine.text())
        self.m_ui.lineEdit_TerminalUserCommandLine.clear()
        #### **** you will have to process this text for the PROP before clearing it...

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
    
        


