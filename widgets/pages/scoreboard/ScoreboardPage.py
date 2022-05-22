from PyQt5.QtWidgets import *

class ScoreboardPage(QFrame):
    def __init__(self, parent):
        super(ScoreboardPage, self).__init__()
        
        self.parent = parent

        self.initUI()

    # Initializes the UI
    def initUI(self):
        pass