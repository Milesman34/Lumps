from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from helper_functions import *

# This widget holds the buttons in charge of controlling dice rolls
class DiceControlBar(QFrame):
    def __init__(self, parent):
        super(DiceControlBar, self).__init__()

        self.parent = parent

        self.initUI()

    # Updates the UI, so that only the needed buttons are displayed
    def updateUI(self):
        # Get rid of the original layout
        if self.layout() is not None:
            QWidget().setLayout(self.layout())

        layout = QHBoxLayout()

        # Button that handles die rolls
        self.diceRollButton = create_push_button(self.parent, "Roll Dice", 18)

        self.diceRollButton.clicked.connect(self.parent.roll_dice)

        # Button that ends the current turn
        self.endTurnButton = create_push_button(self.parent, "End Turn", 18)
        
        self.endTurnButton.clicked.connect(self.parent.end_turn)
        
        # There are several options here
        # If there is not a current turn, then display only the "roll dice" button
        # If there is a current turn, display the "roll dice" and "end turn" buttons
        # If the turn is over, only display the "end turn" button in the place of the "roll dice" button
        # Adds the widgets to the dice control layout, with spacers as needed
        # The left spacer always exists
        add_spacer(layout)

        if not self.parent.is_turn_occurring:
            layout.addWidget(self.diceRollButton, stretch=2)
            add_spacer(layout, 1)
        elif self.parent.has_rolls_remaining():
            layout.addWidget(self.diceRollButton, stretch=2)
            layout.addWidget(self.endTurnButton, stretch=1)
        else:
            layout.addWidget(self.endTurnButton, stretch=1)
            add_spacer(layout, 1)

        self.setLayout(layout)

    # Initializes the UI (the UI is always the same)
    def initUI(self):
        self.updateUI()