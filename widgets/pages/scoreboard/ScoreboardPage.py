from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets.pages.scoreboard.ScoreTable import ScoreTable

from helper_functions import *

class ScoreboardPage(QFrame):
    def __init__(self, parent):
        super(ScoreboardPage, self).__init__()
        
        self.parent = parent

        self.updateUI()

    # Initializes/updates the UI
    def updateUI(self):
        # Get rid of the original layout
        if self.layout() is not None:
            QWidget().setLayout(self.layout())
            
        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Adds the header widget
        headerLabel = QLabel("Scoreboard")
        headerLabel.setFont(QFont("Arial", 18))
        headerLabel.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        # Adds the table for displaying scores
        self.scoreTable = ScoreTable(self.parent)

        # GUI programming is pain because you can't just give the grid rows an arbitrary size
        layout.addWidget(headerLabel, stretch=2)
        layout.addWidget(self.scoreTable, stretch=self.parent.num_turns() * 2)
        add_spacer(layout, stretch=10 - self.parent.num_turns())

        self.setLayout(layout)
