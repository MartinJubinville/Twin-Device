# Copyright (C) 2024 Wild Rose Technologies Inc.
# Note: This program part is called WowSer, but uses Ui_wowserTerminal
#     since it is like a terminal that can come up when requested.

from PySide6.QtCore import Qt, Signal, Slot, QPoint
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit
from PySide6.QtGui import QPalette

from ui_wowserTerminal import Ui_wowserTerminal
from wowserSettings import wowserSettingsDialog # replace SettingsDialog in Sample

# *** From sample
from PySide6.QtCore import QIODeviceBase, Slot, QByteArray
#QByteArray is here for me to test tx on serial 
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox
from PySide6.QtSerialPort import QSerialPort

UNHANDLED_KEYS = [Qt.Key_Backspace, Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down]


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
    get_data = Signal(bytearray)                            # from Sample
    output_tB_MW = Signal(str)  # output to main screen text on main app
    

    # Methods
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_ui = Ui_wowserTerminal()                     # Ui_MainWindow() in Sample
        self.m_status = QLabel()                            # from Sample
        ### self.m_console = Console()                      # in Sample this is a QPlainTextEdit()
        ### self.m_settings = SettingsDialog(self)          # in Sample, but replaced by myWowSerSettingsDialog below
        self.m_serial = QSerialPort(self)

        self.m_ui.setupUi(self)

        #self.m_console.setEnabled(False)               # from Sample
        #self.document().setMaximumBlockCount(100)       # I have a QTextBrowser instead of QTextEdit???


        self.move(QPoint(20, 20))
        # *** Let's try to format the windows for green on black
        # *** Designer crashes in trying to do this, so we will code it
        self.myPalette = self.palette()
        self.myPalette.setColor(QPalette.Base, Qt.black)
        self.myPalette.setColor(QPalette.Text, Qt.green)
        self.setPalette(self.myPalette)


        # Let's try to instantiate WowSerSettings here
        # It will be hierachical and more easier to bring in to other projects
        self.myWowSerSettingsDialog = wowserSettingsDialog()
        self.myWowSerSettingsDialog.show()


        #connections
        self.m_ui.actionWowSerSettings.triggered.connect(self.woswerSettingsWindowShow) ### <----
        self.myWowSerSettingsDialog.m_ui.applyButton.clicked.connect(self.wowserSerialSettingsUpdated)
        #self.m_ui.lineEdit_TerminalUserCommandLine.textChanged.connect(self.echoTerminalText) #need more
        self.m_ui.lineEdit_TerminalUserCommandLine.returnPressed.connect(self.echoTerminalText)

        self.m_ui.actionWowSerTerminalWipe.triggered.connect(self.wowserTerminalClear)
        self.m_ui.actionWowSerDisconnect.triggered.connect(self.close_serial_port)
        self.m_ui.actionWowSerConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionLoadPreviousSettings.triggered.connect(self.loadPreviousSerialSettings)


        ### now to make serial port input / output run
        self.m_serial.readyRead.connect(self.read_data)
        ### *** prop light does go on so now read text from serial is next ToDo

        


    #Slots

    @Slot()
    def loadPreviousSerialSettings(self):
        print("Loading previous serial settings")    
        self.myWowSerSettingsDialog.m_currentSettings.baud_rate = 2000000
        self.myWowSerSettingsDialog.m_currentSettings.name = "/dev/tty.usbserial-P6jfn13t"


    @Slot()
    def wowserTerminalClear(self):
        self.m_ui.textBrowser_TerminalScreen.clear()
        print("Cleared the terminal screen")
        
    @Slot()
    def echoTerminalText(self):
        print("Text was entered in the Terminal")
        self.m_ui.textBrowser_TerminalScreen.append(self.m_ui.lineEdit_TerminalUserCommandLine.text())
        self.m_ui.lineEdit_TerminalUserCommandLine.clear()
        #### **** you will have to process this text for the PROP before clearing it...
        texttx = QByteArray("Hi there prop")
        self.m_serial.write(texttx)     ### test if prop light goes
        ### *** prop light does go on so now read text from serial is next ToDo

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
        self.myWowSerSettingsDialog.raise_()
        self.myWowSerSettingsDialog.show()
        self.myWowSerSettingsDialog.activateWindow()

    @Slot()
    def wowserSerialSettingsUpdated(self):
        print("WowSer serial settings were changed")
        self.raise_()
        print(str(self.myWowSerSettingsDialog.m_currentSettings))
        self.m_ui.textBrowser_TerminalScreen.append("Settings for the serial connection changed.")
        self.m_ui.textBrowser_TerminalScreen.append(description(self.myWowSerSettingsDialog.m_currentSettings))
        self.output_tB_MW.emit("Hi there.")
        #self.output_tB_MW.emit(str(self.myWowSerSettingsDialog.m_currentSettings))
        self.output_tB_MW.emit(description(self.myWowSerSettingsDialog.m_currentSettings))

    ### *** Here are some Slots from the "Console" in Sample to WowSerTerminal
    ### *** to convert resources, change "self" to self.???
        
    @Slot(bytearray)       
    def put_data(self, data):
        self.insertPlainText(data.decode("utf8"))
        bar = self.verticalScrollBar()
        bar.setValue(bar.maximum())

    def set_local_echo_enabled(self, e):
        self.m_localEchoEnabled = e
    """
    def keyPressEvent(self, e):
        key = e.key()
        if key not in UNHANDLED_KEYS:
            if self.m_localEchoEnabled:
                super().keyPressEvent(e)
            self.get_data.emit(e.text().encode())
    """          

    def mousePressEvent(self, e):
        self.setFocus()

    def mouseDoubleClickEvent(self, e):
        pass

    def contextMenuEvent(self, e):
        pass
    
### *** Here are the Slots from Sample in its mainwindow
    @Slot()
    def open_serial_port(self):
        ###s = self.m_settings.settings()
        print("Open serial port signal run")
        s = self.myWowSerSettingsDialog.m_currentSettings
        self.m_serial.setPortName(s.name)
        self.m_serial.setBaudRate(s.baud_rate)
        self.m_serial.setDataBits(s.data_bits)
        self.m_serial.setParity(s.parity)
        self.m_serial.setStopBits(s.stop_bits)
        self.m_serial.setFlowControl(s.flow_control)
        if self.m_serial.open(QIODeviceBase.ReadWrite):
            ### self.m_console.setEnabled(True)
            ### self.m_console.set_local_echo_enabled(s.local_echo_enabled)
            self.m_ui.actionConnect.setEnabled(False)
            self.m_ui.actionDisconnect.setEnabled(True)
###            self.m_ui.actionConfigure.setEnabled(False)  # needs fix
            self.show_status_message(description(s))
            ### emit to mainwindow
            self.output_tB_MW.emit("Serial port opened.")
            print("Serial port opened")
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")

    @Slot()
    def close_serial_port(self):
        print("Close serial port signal run")
        if self.m_serial.isOpen():
            self.m_serial.close()
        ### self.m_console.setEnabled(False)
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)
###        self.m_ui.actionConfigure.setEnabled(True)   # needs fix
        self.show_status_message("Disconnected")
        ### emit to mainwindow
        self.output_tB_MW.emit("Serial port closed.")

    @Slot()
    def about(self):
        QMessageBox.about(self, "About Simple Terminal", HELP)

    @Slot(bytearray)
    def write_data(self, data):
        self.m_serial.write(data)

    @Slot()
    def read_data(self):
        #data = self.m_serial.readAll()  #works !!!
        data = QByteArray(self.m_serial.readAll())  #works !!!

        print("The read_data was called.")
        ### self.m_console.put_data(data.data())
        #self.m_ui.textBrowser_TerminalScreen.put_data(data.data())  ### still has to tested.
        #self.m_ui.textBrowser_TerminalScreen.append(data.decode("utf8"))
        #self.m_ui.textBrowser_TerminalScreen.append(data.data())

        #####iself.m_ui.textBrowser_TerminalScreen.append(str(data, 'utf-8')) #works!!
        #####self.m_ui.textBrowser_TerminalScreen.append(data.toStdString()) #works!!!
        self.m_ui.textBrowser_TerminalScreen.insertPlainText(str(data, 'utf-8'))  #works!!!

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.ResourceError:
            QMessageBox.critical(self, "Critical Error",
                                 self.m_serial.errorString())
            self.close_serial_port()

    @Slot(str)
    def show_status_message(self, message):
        self.m_status.setText(message)        


