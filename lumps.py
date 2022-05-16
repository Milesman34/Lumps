from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QStackedLayout, QLabel, QWidget, QSizePolicy

import helper_functions as helper, enums, sys

# Class for the main window
class Lumps(QMainWindow):
    def __init__(self, width: int, height: int):
        super(Lumps, self).__init__()

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
        # Creates the outer layout
        outerLayout = QVBoxLayout(self)
        outerLayout.setContentsMargins(0, 0, 0, 0)

        # Creates the top object and gives it a border
        upperTabBar = QLabel("Upper Part")
        upperTabBar.setStyleSheet("background-color: rgb(235, 235, 235); border-bottom: 2px solid black;")

        outerLayout.addWidget(upperTabBar, stretch=1)
        outerLayout.addWidget(QLabel("Bottom Part"), stretch=19)

        # Creates the main widget
        mainWidget = QWidget()
        mainWidget.setLayout(outerLayout)

        self.setCentralWidget(mainWidget)

        # # Stacked layout to use
        # layout = QStackedLayout()

        # layout.addWidget(QLabel("Dice page"))
        # layout.addWidget(QLabel("Scoreboard page"))

        # layout.setCurrentIndex(1)

        # # Central widget
        # widget = QWidget()
        # widget.setLayout(layout)

        # self.setCentralWidget(widget)


# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Creates the new window
    window = Lumps(1280, 720)
    window.show()

    app.exec()


if __name__ == "__main__":
    main_window()