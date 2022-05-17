from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from helper_functions import *

# This dialog gets the number of players
class PlayerCountDialog(QDialog):
    # Startup variable tracks if this was called on startup
    def __init__(self, min_players: int, max_players: int):
        super().__init__()

        # Sets important attributes of the dialog window
        self.setWindowTitle("Enter Number of Players")
        self.setWindowModality(Qt.ApplicationModal)

        # Key values for this dialog
        self.min_players = min_players
        self.max_players = max_players

        # This value represents the number of players
        self.count = -1

        self.initUI()

        self.exec()

    # Sets up the UI for the dialog
    def initUI(self):
        # Creates the main layout
        layout = QVBoxLayout(self)

        # Text for telling the user what to do
        layout.addWidget(QLabel(f"Enter a number between {self.min_players} and {self.max_players}"))

        # Textbox for user input
        self.textbox = QLineEdit(self)

        layout.addWidget(self.textbox)

        # Textbox that tells the user if they inputted something incorrectly
        self.error_text = QLabel("")
        self.error_text.setStyleSheet("color: red;")

        layout.addWidget(self.error_text)

        # Button to submit the number of players
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout.addWidget(buttonBox)

        # Action for when the form is accepted
        buttonBox.accepted.connect(self.handleInput)

        # Action for when the form is rejected
        buttonBox.rejected.connect(self.reject)

        # Sets the layout for the dialog
        self.setLayout(layout)

    # Handles the user's input, returning it if possible and providing feedback for any mistakes
    def handleInput(self):
        text = self.textbox.text().strip()

        if len(text) == 0:
            self.error_text.setText("Input cannot be empty")
        elif not(str_is_int(text)):
            self.error_text.setText("Input must be an integer")
        else:
            value = int(text)

            if value <= 0:
                self.error_text.setText("Input must be positive")
            elif value < self.min_players or value > self.max_players:
                self.error_text.setText(f"Input must be between {self.min_players} and {self.max_players}")
            else:
                self.count = value
                self.close()