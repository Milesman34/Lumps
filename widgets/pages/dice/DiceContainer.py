from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from widgets.pages.dice.DieWidget import DieWidget

# This widget contains all the dice for the game
class DiceContainer(QFrame):
    def __init__(self, parent):
        super(DiceContainer, self).__init__()

        self.parent = parent

        self.resetLayout()

    # Resets the layout to show the current dice
    def resetLayout(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # The locked dice go first
        for die in self.parent.locked_dice + self.parent.available_dice:
            layout.addWidget(DieWidget(self.parent, die))

        self.setLayout(layout)