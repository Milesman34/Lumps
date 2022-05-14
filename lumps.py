from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPoint

import helper_functions as helper, sys

# Class for the main window
class Lumps(QMainWindow):
    def __init__(self, width: int, height: int):
        super(Lumps, self).__init__()

        # Sets the properties of the window
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Lumps")

        # Dimensions of window
        self.width = width
        self.height = height

        # Initializes the UI
        self.initUI()

    # Initializes the UI
    def initUI(self):
        pass

# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Creates the new window
    window = Lumps(1280, 720)

    window.show()
    app.exec()


if __name__ == "__main__":
    main_window()