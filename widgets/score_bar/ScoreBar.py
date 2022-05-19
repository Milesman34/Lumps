from PyQt5.QtWidgets import *

from widgets.score_bar.ScoreBarLabel import ScoreBarLabel

# Class that represents the score bar
class ScoreBar(QFrame):
    def __init__(self, parent):
        super(ScoreBar, self).__init__()

        self.parent = parent

        self.resetLayout()

    # Resets the layout to match the current scores
    def resetLayout(self):
        scoresLayout = QHBoxLayout(self)

        scoresLayout.setContentsMargins(0, 0, 0, 0)

        # Creates and adds a label for each score
        for index, score in enumerate(self.parent.scores):
            label = ScoreBarLabel(index, score)

            scoresLayout.addWidget(label)

        self.setLayout(scoresLayout)