from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from widgets.pages.dice.DieWidget import DieWidget

from helper_functions import *

# This widget contains all the dice for the game
class DiceContainer(QFrame):
    def __init__(self, parent):
        super(DiceContainer, self).__init__(parent)

        self.parent = parent

        self.initUI()

    # Updates the UI to show the current dice
    def updateUI(self):
        # Get rid of the original layout
        if self.layout() is not None:
            QWidget().setLayout(self.layout())

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        # The widgets should only be added if there is a turn occurring
        if self.parent.is_turn_occurring:
            for die in sort_dice(self.parent.dice):
                layout.addWidget(DieWidget(self.parent, die))

        self.setLayout(layout)

    # Initializes the UI (the UI is always the same)
    def initUI(self):
        self.updateUI()