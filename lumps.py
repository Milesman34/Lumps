from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QTabWidget

from widgets.BottomTabButton import BottomTabButton

import enums, sys

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

        # Eliminates the margins between each element
        outerLayout.setContentsMargins(0, 0, 0, 0)

        # Creates the top bar and gives it a border
        upperTabBar = QLabel("Upper Part")
        upperTabBar.setStyleSheet("background-color: rgb(235, 235, 235); border-bottom: 2px solid black;")

        # Creates the bottom bar and gives it a border
        bottomTabBar = QWidget()
        
        # The object has its own name so that the children do not also get the same styling
        bottomTabBar.setObjectName("bottomTabBar")
        bottomTabBar.setStyleSheet("QWidget#bottomTabBar {background-color: rgb(235, 235, 235); border-top: 2px solid black;}")
        
        bottomTabBarLayout = QHBoxLayout(self)

        # Creates the two buttons for the bottom tab bar to switch pages
        self.dicePageButton = BottomTabButton(self, "Dice")
        self.scoreboardPageButton = BottomTabButton(self, "Scoreboard")

        # Adds the two button widgets to the bottom tab bar
        bottomTabBarLayout.addWidget(self.dicePageButton)
        bottomTabBarLayout.addWidget(self.scoreboardPageButton)

        bottomTabBar.setLayout(bottomTabBarLayout)

        # Adds the widgets to the outer layout
        outerLayout.addWidget(upperTabBar, stretch=1)
        outerLayout.addWidget(QLabel("Middle Part"), stretch=18)
        outerLayout.addWidget(bottomTabBar, stretch=1)

        # Creates the main widget
        mainWidget = QWidget()
        mainWidget.setLayout(outerLayout)

        self.setCentralWidget(mainWidget)


# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Creates the new window
    window = Lumps(1280, 720)
    window.show()

    app.exec()


if __name__ == "__main__":
    main_window()