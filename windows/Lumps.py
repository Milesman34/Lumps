from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from classes.Die import Die

from widgets.BottomTabButton import BottomTabButton

import enums

# Class for the main window
class Lumps(QMainWindow):
    def __init__(self, width: int, height: int, players: int):
        super(Lumps, self).__init__()

        # Sets the properties of the window
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Lumps")

        # Current page in the app
        self.current_page = enums.AppPage.DICE

        # Current number of points
        self.points = 0

        # Current number of rolls left
        self.rolls = 3

        # Number of players
        self.players = players

        # Scores from each player
        self.scores = [0] * self.players

        # List of dice, both the available and locked ones
        self.number_of_dice = 8

        self.available_dice = [Die(4), Die(4), Die(6), Die(6), Die(8), Die(8), Die(10), Die(10)]
        self.locked_dice = []

        print(self.available_dice)
        
        self.initUI()

    # Initializes the UI
    def initUI(self):
        # Creates the outer layout
        outerLayout = QVBoxLayout(self)

        # Eliminates the margins between each element
        outerLayout.setContentsMargins(0, 0, 0, 0)

        # Creates the top bar and gives it a border
        upperTabBar = QLabel("Upper Part")
        upperTabBar.setStyleSheet("background-color: rgb(235, 235, 235); border-bottom: 2px solid black;")

        # Creates the scores area
        self.scoresBar = QWidget()
        self.scoresBar.setObjectName("scoresBar")
        self.scoresBar.setStyleSheet("QWidget#scoresBar {background-color: rgb(235, 235, 235); border-bottom: 2px solid black;}")

        self.resetScoreElementsLayout()

        # Creates the central part of the app
        self.centralPart = QStackedWidget()

        # Adds the two currently existing pages (pages not implemented yet)
        self.centralPart.addWidget(QLabel("Dice"))
        self.centralPart.addWidget(QLabel("Scoreboard"))

        # Sets the current page
        self.centralPart.setCurrentIndex(enums.AppPage.DICE.value)

        # Creates the bottom bar and gives it a border
        bottomTabBar = QWidget()
        
        # The object has its own name so that the children do not also get the same styling
        bottomTabBar.setObjectName("bottomTabBar")
        bottomTabBar.setStyleSheet("QWidget#bottomTabBar {background-color: rgb(235, 235, 235); border-top: 2px solid black;}")
        bottomTabBar.setContentsMargins(0, 0, 0, 0)
        
        bottomTabBarLayout = QHBoxLayout(self)

        # Creates the two buttons for the bottom tab bar to switch pages
        self.dicePageButton = BottomTabButton(self, "Dice", enums.AppPage.DICE)
        self.scoreboardPageButton = BottomTabButton(self, "Scoreboard", enums.AppPage.SCOREBOARD)

        # Adds the two button widgets to the bottom tab bar
        bottomTabBarLayout.addWidget(self.dicePageButton)
        bottomTabBarLayout.addWidget(self.scoreboardPageButton)

        bottomTabBar.setLayout(bottomTabBarLayout)

        # Adds the widgets to the outer layout
        outerLayout.addWidget(upperTabBar, stretch=1)
        outerLayout.addWidget(self.scoresBar, stretch=1)
        outerLayout.addWidget(self.centralPart, stretch=17)
        outerLayout.addWidget(bottomTabBar, stretch=1)

        # Creates the main widget
        mainWidget = QWidget()
        mainWidget.setLayout(outerLayout)

        self.setCentralWidget(mainWidget)

    # Resets the score elements by replacing the layout of the scores bar
    def resetScoreElementsLayout(self):
        scoresLayout = QHBoxLayout(self)

        # Creates and adds a label for each score
        for index, score in enumerate(self.scores):
            label = QLabel(f"Player {index + 1}: {score}")

            label.setFont(QFont("Arial", 15))
            label.setAlignment(Qt.AlignCenter)

            scoresLayout.addWidget(label)

        self.scoresBar.setLayout(scoresLayout)
