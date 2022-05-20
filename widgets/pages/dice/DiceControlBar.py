from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        diceRollButton = QPushButton(self.parent)
        diceRollButton.setText("Roll Dice")
        diceRollButton.setFont(QFont("Arial", 18))

        diceRollButton.clicked.connect(self.parent.roll_dice)
        
        # Adds the widgets to the dice control layout, with spacers as needed
        layout.addWidget(QFrame())
        layout.addWidget(diceRollButton)
        layout.addWidget(QFrame())

        self.setLayout(layout)