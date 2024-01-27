# Copyright (C) 2024 Wild Rose Technologies Inc.

import sys

from PySide6.QtCore import Slot

from PySide6.QtGui import QIntValidator 
from PySide6.QtWidgets import QComboBox
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from PySide6.QtWidgets import QDialog

from ui_dialogsecondwindow import Ui_DialogSecondWindow


class mySerialSettings():
    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.string_baud_rate = ""
        self.data_bits = QSerialPort.Data8
        self.string_data_bits = ""
        self.parity = QSerialPort.NoParity
        self.string_parity = ""
        self.stop_bits = QSerialPort.OneStop
        self.string_stop_bits = ""
        self.flow_control = QSerialPort.SoftwareControl
        self.string_flow_control = ""
        self.local_echo_enabled = False

class DialogSecondWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_ui = Ui_DialogSecondWindow()
        self._custom_port_index = -1
        self.m_ui.setupUi(self)