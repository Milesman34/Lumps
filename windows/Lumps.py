from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from classes.Die import Die
from helper_functions import calculate_lumps_score

from widgets.bottom_bar.BottomBar import BottomBar
from widgets.score_bar.ScoreBar import ScoreBar

from widgets.pages.dice.DicePage import DicePage

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

        # Index of current player
        self.current_player = 0

        # Number of players
        self.players = players

        # Scores from each player
        self.scores = [0] * self.players

        # List of dice to create
        self.default_dice = [4, 4, 6, 6, 8, 8, 10, 10]

        # List of dice, both the available and locked ones
        self.number_of_dice = 8

        self.available_dice = []
        self.locked_dice = []

        # Is a turn taking place
        self.is_turn_occurring = False
        
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
        self.dicePage = DicePage(self)

        self.centralPageWidget.addWidget(self.dicePage)
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

    # Populates the list of available dice
    def populate_available_dice(self):
        self.available_dice = [Die(i) for i in self.default_dice]

    # Attempts to roll the dice
    def roll_dice(self):
        # If there is no turn occurring, then it needs to populate the list of available dice
        if not self.is_turn_occurring:
            self.is_turn_occurring = True
            self.populate_available_dice()

        # If there are no rolls left, then move to the next player
        if self.rolls_left == 0:
            self.current_player = (self.current_player + 1) % self.players
            self.rolls_left = 3
        
        self.rolls_left -= 1
        self.roll_available()

        self.points = calculate_lumps_score(self.available_dice + self.locked_dice)

        # Updates information labels on the dice page
        self.dicePage.updateUI()

    # Rolls all the available dice
    def roll_available(self):
        for die in self.available_dice:
            die.roll()

        self.available_dice = sorted(self.available_dice, key=lambda e: (e.value, e.sides))
