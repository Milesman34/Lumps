from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# This class represents an entry in the score bar for showing the scores
class ScoreBarLabel(QWidget):
    def __init__(self, index: int, score: int):
        super().__init__()

        self.index = index + 1
        self.score = score

        self.initUI()
    
    # Sets up the UI
    def initUI(self):
        layout = QHBoxLayout()
        
        # Displays the player's ID
        labelPlayer = QLabel(f"Player {self.index}: ")
        labelPlayer.setFont(QFont("Arial", 12))
        labelPlayer.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Displays the player's score
        labelScore = QLabel(str(self.score))
        labelScore.setFont(QFont("Arial", 18))
        labelScore.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        layout.addWidget(labelPlayer)
        layout.addWidget(labelScore)

        self.setLayout(layout)