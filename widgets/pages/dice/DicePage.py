from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Page for showing the dice and core gameplay
class DicePage(QFrame):
    def __init__(self, parent):
        super(DicePage, self).__init__()

        self.parent = parent

        self.initUI()

    # Initializes the UI
    def initUI(self):
        layout = QVBoxLayout()

        # The information display shows core information about the current term
        self.informationDisplay = QFrame()
        infoLayout = QVBoxLayout()

        # Creates the widgets that display key information
        self.playerLabel = QLabel("Player 1's Turn")
        self.playerLabel.setAlignment(Qt.AlignCenter)

        self.scoreLabel = QLabel("0")
        self.scoreLabel.setAlignment(Qt.AlignCenter)
        self.scoreLabel.setFont(QFont("Arial", 18))

        self.rollsLabel = QLabel("3 rolls left")
        self.rollsLabel.setAlignment(Qt.AlignCenter)

        infoLayout.addWidget(self.playerLabel, stretch=1)
        infoLayout.addWidget(self.scoreLabel, stretch=3)
        infoLayout.addWidget(self.rollsLabel, stretch=1)

        self.informationDisplay.setLayout(infoLayout)

        # Creates the QFrame to hold the dice
        self.diceCentralArea = QFrame()
        self.diceControlBar = QLabel("Dice control")

        layout.addWidget(self.informationDisplay, stretch=3)
        layout.addWidget(self.diceCentralArea, stretch=16)
        layout.addWidget(self.diceControlBar, stretch=1)

        self.setLayout(layout)