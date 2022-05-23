from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from typing import List

# Class that represents the widget for displaying the cumulative scores
class ScoreTable(QFrame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.updateUI()

    # Returns the list of elements to display
    # First row is the header, other rows consist of the scores
    def getElements(self) -> List[List[str]]:
        return [[f"Player {index + 1}"] + ['--' if i is None else str(i) for i in self.parent.scoreboard[index]] for index in range(self.parent.players)]

    # Updates the UI
    def updateUI(self):
        # Get rid of the original layout
        if self.layout() is not None:
            QWidget().setLayout(self.layout())

        layout = QGridLayout()

        layout.setSpacing(0)

        elements = self.getElements()

        # Displays each label in the 2D list of elements to display
        for col_index, col in enumerate(elements):
            for row_index, row in enumerate(col):
                # Creates the new label widget
                label = QLabel(row)
                
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("border: 2px solid black;")
                layout.addWidget(label, row_index, col_index)

        self.setLayout(layout)

