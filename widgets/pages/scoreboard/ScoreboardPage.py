from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from helper_functions import *

class ScoreboardPage(QFrame):
    def __init__(self, parent):
        super(ScoreboardPage, self).__init__()
        
        self.parent = parent

        self.initUI()

    # Initializes the UI
    def initUI(self):
        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        # Adds the header widget
        headerLabel = QLabel("Scoreboard")
        headerLabel.setFont(QFont("Arial", 18))
        headerLabel.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        layout.addWidget(headerLabel, stretch=1)
        add_spacer(layout, 9)
        

        self.setLayout(layout)
