from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QLabel, QWidget

import helper_functions as helper, enums, sys

# Class for the main window
class Lumps(QMainWindow):
    def __init__(self, width: int, height: int, parent=None):
        super(Lumps, self).__init__(parent)

        # Sets the properties of the window
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Lumps")
        
        self.initUI()

        # Current page in the app
        self.current_page = enums.AppPage.DICE

        # Current number of points
        self.points = 0

        # Current number of rolls left
        self.rolls = 3

    # Initializes the UI
    def initUI(self):
        # Stacked layout to use
        layout = QStackedLayout()

        layout.addWidget(QLabel("Dice page"))
        layout.addWidget(QLabel("Scoreboard page"))

        layout.setCurrentIndex(1)

        # Central widget
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Creates the new window
    window = Lumps(1280, 720)
    window.show()

    app.exec()


if __name__ == "__main__":
    main_window()