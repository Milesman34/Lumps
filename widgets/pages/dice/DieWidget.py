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

    # Responds to a left-click
    def mousePressEvent(self, event):
        # This event only occurs if the die is unlocked and there are rolls remaining
        if event.button() == Qt.LeftButton and not self.die.locked and self.parent.has_rolls_remaining():
            self.toggleLock()

    # Responds to mouse over enter
    def enterEvent(self, event):
        if not self.die.locked:
            self.setStyleSheet("QFrame#dieWidget {background-color: rgb(255, 255, 255); border: 2px solid black;}")

    # Responds to mouse exit event
    def leaveEvent(self, event):
        if not self.die.locked:
            self.setStyleSheet("QFrame#dieWidget {background-color: rgb(235, 235, 235); border: 2px solid black;}")

    # Toggles if the die is locked, but it won't be permanently locked until the roll dice button is clicked
    def toggleLock(self):
        self.die.temp_locked = not self.die.temp_locked
        self.updateLockedWidget()

    # Updates the locked widget text
    def updateLockedWidget(self):
        self.lockedWidget.setText("Locked" if self.die.temp_locked else "")
    
    # Initializes the UI
    def initUI(self):
        # Widget should have a fixed size
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setObjectName("dieWidget")

        # The stylesheet color depends on if the die is locked
        if self.die.locked:
            self.setStyleSheet("QFrame#dieWidget {background-color: rgb(200, 200, 200); border: 2px solid black;}")
        else:
            self.setStyleSheet("QFrame#dieWidget {background-color: rgb(235, 235, 235); border: 2px solid black;}")

        # Creates the layout for this widget
        layout = QVBoxLayout()

        self.sidesWidget = QLabel(f"{self.die.sides} sides")
        self.valueWidget = QLabel(f"{self.die.value}")
        self.valueWidget.setFont(QFont("Arial", 14))
        self.lockedWidget = QLabel()
        self.updateLockedWidget()

        self.sidesWidget.setAlignment(Qt.AlignCenter)
        self.valueWidget.setAlignment(Qt.AlignCenter)
        self.lockedWidget.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.sidesWidget, stretch=1)
        layout.addWidget(self.valueWidget, stretch=5)
        layout.addWidget(self.lockedWidget, stretch=1)

        self.setLayout(layout)