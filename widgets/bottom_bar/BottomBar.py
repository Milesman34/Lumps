from PyQt5.QtWidgets import *

from widgets.bottom_bar.BottomTabButton import BottomTabButton

import enums

# This class represents the bar at the bottom for switching pages
class BottomBar(QFrame):
    def __init__(self, parent):
        super(BottomBar, self).__init__()

        self.parent = parent

        self.initUI()

    # Initializes the UI
    def initUI(self):
        self.setObjectName("bottomTabBar")
        self.setStyleSheet("QWidget#bottomTabBar {background-color: rgb(235, 235, 235); border-top: 2px solid black;}")
        
        layout = QHBoxLayout(self)

        # Creates the two buttons for the bottom tab bar to switch pages
        self.dicePageButton = BottomTabButton(self.parent, "Dice", enums.AppPage.DICE)
        self.scoreboardPageButton = BottomTabButton(self.parent, "Scoreboard", enums.AppPage.SCOREBOARD)

        # Adds the two button widgets to the bottom tab bar
        layout.addWidget(self.dicePageButton)
        layout.addWidget(self.scoreboardPageButton)

        self.setLayout(layout)