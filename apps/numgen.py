#!/usr/bin/env python3

"""
App module for generating a random number.
"""

import sys
import random

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDockWidget,
                             QWidget, QHBoxLayout, QPushButton, QLabel)

from swift.app import BaseApp

class _NumGenFrame(QWidget):
    """Frame class for showing the button and the label."""
    def __init__(self):
        super().__init__()
        self.init_widget()

    def init_widget(self):
        """Initializes widgets in the frame."""
        self.btn = QPushButton("generate number", self)
        self.label = QLabel("not generated", self)

        layout = QHBoxLayout(self)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)


class NumGenApp(BaseApp):
    """App class for managing a frame and generating a random number.

    Attributes:
        frame: A frame that request generating and show a random number.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.frame = _NumGenFrame()

        # connect the button clicked signal to the slot generating a number
        self.frame.btn.clicked.connect(self.generateNumber)

    def frames(self):
        return (self.frame,)

    @pyqtSlot()
    def generateNumber(self):
        """Generates and shows a random number when the button is clicked."""
        num = random.randrange(0, 10)

        self.frame.label.setText(f"generated number: {num}")


def main():
    """Main function that runs when numgen.py is called."""
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    # create a app
    app = NumGenApp("numgen")

    # get frames from the app and add them as dock widgets
    for frame in app.frames():
        dock_widget = QDockWidget("random number generator", main_window)
        dock_widget.setWidget(frame)

        main_window.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()