from PyQt5 import QtCore, QtWidgets, QtGui

# Main class that represents the UI
class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, app, width: int, height: int):
        # Sets the properties of the window
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Lumps")

        # Dimensions of window
        self.width = width
        self.height = height
        
        # QTStack for handling both main pages
        self.QtStack = QtWidgets.QStackedLayout()
