from PyQt5 import QtWidgets

class BottomTabButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, text=""):
        super(BottomTabButton, self).__init__(parent)

        # Sets the text of the button
        self.setText(text)

        self.setStyleSheet("background-color: rgb(235, 235, 235);")