from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from helper_functions import *

# This widget holds the buttons in charge of controlling dice rolls
class DiceControlBar(QFrame):
    def __init__(self, parent):
        super(DiceControlBar, self).__init__()

        self.parent = parent

        self.initUI()

    # Initializes the UI
    def initUI(self):
        layout = QHBoxLayout()

        # Button that handles die rolls
        self.diceRollButton = create_push_button(self.parent, "Roll Dice", 18)

        self.diceRollButton.clicked.connect(self.parent.roll_dice)

        # Button that ends the current turn
        self.endTurnButton = create_push_button(self.parent, "End Turn", 18)
        
        # Adds the widgets to the dice control layout, with spacers as needed
        layout.addWidget(QFrame())
        layout.addWidget(self.diceRollButton)
        layout.addWidget(self.endTurnButton)
        layout.addWidget(QFrame())

        self.setLayout(layout)