# Copyright (C) 2024 Wild Rose Technologies Inc.
# Let's see about making changes for Git.
# Second test
# Edited on mac and pushed, etc from there

import sys

"""Driving the Twin Device from Wild Rose Technologies, Inc."""

from PySide6.QtWidgets import QApplication

from mainwindow import TwinDeviceMainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TwinDeviceMainWindow()
    window.show()

    sys.exit(app.exec())
