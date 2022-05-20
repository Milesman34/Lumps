from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from helper_functions import *

from widgets.pages.dice.DiceContainer import DiceContainer

# Page for showing the dice and core gameplay
class DicePage(QFrame):
    def __init__(self, parent):
        super(DicePage, self).__init__()

        self.parent = parent

        self.initUI()

        self.updateLabels()

    # Updates the text on labels
    def updateLabels(self):
        self.playerLabel.setText(f"Player {self.parent.current_player + 1}'s turn")

        self.scoreLabel.setText(str(self.parent.points))

        # The rolls may need to be pluralized
        self.rollsLabel.setText(format_rolls_left(self.parent.rolls_left))

    # Initializes the UI
    def initUI(self):
        layout = QVBoxLayout()

        # The information display shows core information about the current term
        self.informationDisplay = QFrame()
        infoLayout = QVBoxLayout()

        # Creates the widgets that display key information
        self.playerLabel = QLabel()
        self.playerLabel.setAlignment(Qt.AlignCenter)

        self.scoreLabel = QLabel()
        self.scoreLabel.setAlignment(Qt.AlignCenter)
        self.scoreLabel.setFont(QFont("Arial", 18))

        self.rollsLabel = QLabel()
        self.rollsLabel.setAlignment(Qt.AlignCenter)

        infoLayout.addWidget(self.playerLabel, stretch=1)
        infoLayout.addWidget(self.scoreLabel, stretch=3)
        infoLayout.addWidget(self.rollsLabel, stretch=1)

        self.informationDisplay.setLayout(infoLayout)

        # Creates the QFrame to hold the dice
        self.diceCentralArea = DiceContainer(self.parent)

        # Creates the widget to handle rolling the dice
        self.diceControlBar = QLabel("Dice control")

        layout.addWidget(self.informationDisplay, stretch=3)
        layout.addWidget(self.diceCentralArea, stretch=8)
        layout.addWidget(QFrame(), stretch=8)
        layout.addWidget(self.diceControlBar, stretch=1)

        self.setLayout(layout)