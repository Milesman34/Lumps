from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from helper_functions import *

from widgets.pages.dice.DiceContainer import DiceContainer
from widgets.pages.dice.DiceControlBar import DiceControlBar

# Page for showing the dice and core gameplay
class DicePage(QFrame):
    def __init__(self, parent):
        super(DicePage, self).__init__()

        self.parent = parent

        self.initUI()

        self.updateUI()

    # Updates the text on labels and the dice display
    def updateUI(self):
        self.playerLabel.setText(f"Player {self.parent.current_player + 1}'s turn")

        self.scoreLabel.setText(str(self.parent.points))

        # The rolls may need to be pluralized
        # If there are 6 or more locked dice then the player cannot roll again anyway
        self.rollsLabel.setText(format_rolls_left(self.parent.rolls_left if self.parent.num_locked_dice() < 6 else 0))

        # This only needs to be updated in some scenarios (if the player needs to keep dice)
        must_keep = self.parent.dice_must_keep()

        if must_keep > 0:
            self.diceToKeepLabel.setText(f"Keep {must_keep} dice this turn")
        else:
            self.diceToKeepLabel.setText("")

        # Updates the dice displayed
        self.diceContainer.updateUI()

        # Updates the elements in the dice control bar
        self.diceControlBar.updateUI()

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

        self.diceToKeepLabel = QLabel()
        self.diceToKeepLabel.setAlignment(Qt.AlignCenter)

        infoLayout.addWidget(self.playerLabel, stretch=1)
        infoLayout.addWidget(self.scoreLabel, stretch=3)
        infoLayout.addWidget(self.rollsLabel, stretch=1)
        infoLayout.addWidget(self.diceToKeepLabel, stretch=1)

        self.informationDisplay.setLayout(infoLayout)

        layout.addWidget(self.informationDisplay, stretch=3)

        # Creates the QFrame to hold the dice
        # This should only display when a turn is occurring
        self.diceContainer = DiceContainer(self.parent)

        layout.addWidget(self.diceContainer, stretch=8)

        # Extra QFrame is blank for now
        add_spacer(layout, 4)

        # Creates the widget to handle rolling the dice
        self.diceControlBar = DiceControlBar(self.parent)
        
        layout.addWidget(self.diceControlBar, stretch=4)

        self.setLayout(layout)