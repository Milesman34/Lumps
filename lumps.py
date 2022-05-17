from PyQt5.QtWidgets import *

from windows.Lumps import Lumps
from windows.PlayerCountDialog import PlayerCountDialog

import sys

# Function for handling the window
def main_window():
    app = QApplication(sys.argv)

    # Gets the nubmer of players from the user
    players_dialog = PlayerCountDialog(1, 8)

    # Creates the new window if the count was valid
    # If it is -1 then that means the app will not run since the startup dialog was closed
    if players_dialog.count != -1:
        window = Lumps(1280, 720, players_dialog.count)
        window.show()

        app.exec()


if __name__ == "__main__":
    main_window()