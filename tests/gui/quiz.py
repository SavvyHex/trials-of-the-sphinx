from PyQt5 import QtWidgets, uic
import sys

class App(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(App, self).__init__()
        uic.loadUi("tests\gui\gui\question.ui", self)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    app.exec_()