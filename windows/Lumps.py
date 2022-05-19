from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from classes.Die import Die

from widgets.bottom_bar.BottomBar import BottomBar
from widgets.score_bar.ScoreBar import ScoreBar

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
        self.rolls_left = 3

        # Number of players
        self.players = players

        # Scores from each player
        self.scores = [0] * self.players

        # List of dice to create
        self.default_dice = [4, 4, 6, 6, 8, 8, 10, 10]

        # List of dice, both the available and locked ones
        self.number_of_dice = 8

        self.available_dice = [Die(d) for d in self.default_dice]
        self.locked_dice = []
        
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
        self.scoresBar = ScoreBar(self)

        # Creates the widget for the central pages of the app
        self.centralPageWidget = QStackedWidget()

        # Adds the two currently existing pages (pages not implemented yet)
        self.centralPageWidget.addWidget(QLabel("Dice"))
        self.centralPageWidget.addWidget(QLabel("Scoreboard"))

        # Sets the current page
        self.centralPageWidget.setCurrentIndex(enums.AppPage.DICE.value)

        # Creates the bottom tab bar
        bottomTabBar = BottomBar(self)

        # Adds the widgets to the outer layout
        outerLayout.addWidget(upperTabBar, stretch=1)
        outerLayout.addWidget(self.scoresBar, stretch=1)
        outerLayout.addWidget(self.centralPageWidget, stretch=17)
        outerLayout.addWidget(bottomTabBar, stretch=1)

        # Creates the main widget
        mainWidget = QWidget()
        mainWidget.setLayout(outerLayout)

        self.setCentralWidget(mainWidget)
