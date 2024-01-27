# Copyright (C) 2024 Wild Rose Technologies Inc.

import sys

from PySide6.QtWidgets import QDialog

from PySide6.QtCore import Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QComboBox
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from PySide6.QtWidgets import QDialog

from ui_wowserSettings import Ui_SettingsDialog


BLANK_STRING = "N/A"

CUSTOM_BAUDRATE_INDEX = 4

class wowserSettingsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_ui = Ui_SettingsDialog()

        self.m_ui.setupUi(self)



