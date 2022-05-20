from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from classes.Die import Die

# Widget that represents a single die in the game
class DieWidget(QFrame):
    def __init__(self, parent, die: Die):
        super(DieWidget, self).__init__()

        self.parent = parent

        # Key values of the die
        self.die = die

        self.initUI()
    
    # Initializes the UI
    def initUI(self):
        # Widget should have a fixed size
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.resize(50, 50)

        self.setObjectName("dieWidget")
        self.setStyleSheet("QFrame#dieWidget {border: 2px solid black;}")

        # Creates the layout for this widget
        layout = QVBoxLayout()

        self.sidesWidget = QLabel(f"{self.die.sides} sides")
        self.valueWidget = QLabel(f"{self.die.value}")
        self.lockedWidget = QLabel("Locked" if self.die.locked else "Unlocked")

        self.sidesWidget.setAlignment(Qt.AlignCenter)
        self.valueWidget.setAlignment(Qt.AlignCenter)
        self.lockedWidget.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.sidesWidget, stretch=1)
        layout.addWidget(self.valueWidget, stretch=5)
        layout.addWidget(self.lockedWidget, stretch=1)

        self.setLayout(layout)