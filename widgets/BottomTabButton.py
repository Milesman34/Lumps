from PyQt5 import QtWidgets

from enums import AppPage


class BottomTabButton(QtWidgets.QPushButton):
    def __init__(self, parent, text, app_page: AppPage):
        super(BottomTabButton, self).__init__(parent)

        # Sets the text of the button
        self.setText(text)

        self.setStyleSheet("background-color: rgb(235, 235, 235);")

        # Adds the on-click event
        self.clicked.connect(lambda e: parent.centralPart.setCurrentIndex(app_page.value))