import sys
from ui import Ui_ivsmath
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.Qt import Qt


class CalculatorWindow(QWidget):
    def __init__(self):
        super(CalculatorWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ivsmath()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.test)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.prdel()

    def test(self):
        print("presseeeed")

    def prdel(self):
        print("prdeel")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())