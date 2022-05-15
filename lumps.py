from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPoint

import helper_functions as helper, enums, sys

from ui_main import Ui_Main

# Class for the main window
class Lumps(QMainWindow, Ui_Main):
    def __init__(self, width: int, height: int):
        super(Lumps, self).__init__()
        self.setupUi(self, width, height)

        # Variable that represents the current window page
        self.current_page = enums.CurrentPage.DICE

        # Current number of points
        self.points = 0

        # Current number of rolls left
        self.rolls = 3

# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Creates the new window
    window = Lumps(1280, 720)

    window.show()
    app.exec()


if __name__ == "__main__":
    main_window()