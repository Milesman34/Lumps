from PyQt5.QtWidgets import *

from widgets.score_bar.ScoreBarLabel import ScoreBarLabel

# Class that represents the score bar
class ScoreBar(QFrame):
    def __init__(self, parent):
        super(ScoreBar, self).__init__()

        self.parent = parent

        self.initUI()

        self.update_UI()

    # Initializes the UI
    def initUI(self):
        self.setObjectName("scoresBar")
        self.setStyleSheet("QFrame#scoresBar {background-color: rgb(235, 235, 235); border-bottom: 2px solid black;}")

    # Updates the UI to match the current scores
    def update_UI(self):
        scoresLayout = QHBoxLayout(self)

        scoresLayout.setContentsMargins(0, 0, 0, 0)

        # Creates and adds a label for each score
        for index, score in enumerate(self.parent.scores):
            label = ScoreBarLabel(index, score)

            scoresLayout.addWidget(label)

        self.setLayout(scoresLayout)