import sys
from ui import Ui_ivsmath
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QFont, QColor, QTextCharFormat
from PyQt5.Qt import Qt, QColor



class CalculatorWindow(QWidget):
    def __init__(self):
        super(CalculatorWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ivsmath()
        self.ui.setupUi(self)

        # self.ui.pushButton_1.clicked.connect(self.test)

        transparentcolor = QColor()
        transparentcolor.setAlpha(0)
        # pen = QPen()
        # pen.setColor(transparentcolor)


        deffont = QFont("Sans Serif")
        deffont.setPixelSize(20)
        deffont.setFamily("Sans Serif")

        textformat = QTextCharFormat()
        textformat.setFont(deffont)
        # textformat.setTextOutline(pen)

        self.scene = QGraphicsScene()

        self.scene.setBackgroundBrush(transparentcolor)
        self.scene.addText("Hovno" , deffont)
        self.scene.clearSelection()
        QGraphicsView(self.scene, self)



    __text__ = ""
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.appendText("1")
        if event.key() == Qt.Key_2:
            self.appendText("2")
        if event.key() == Qt.Key_3:
            self.appendText("3")
        if event.key() == Qt.Key_4:
            self.appendText("4")
        if event.key() == Qt.Key_5:
            self.appendText("5")
        if event.key() == Qt.Key_6:
            self.appendText("6")
        if event.key() == Qt.Key_7:
            self.appendText("7")
        if event.key() == Qt.Key_8:
            self.appendText("8")
        if event.key() == Qt.Key_9:
            self.appendText("9")
        if event.key() == Qt.Key_0:
            self.appendText("0")

    def appendText(self, str:str, sep=''):
        self.__text__ += str
        if sep == '':
            self.__text__ += " "
        QGraphicsView(self.scene, self)

    def clearText(self):
        self.__text__ = ""

    def delText(self):
        if len(self.__text__) == 1:
            self.clearText()
            QGraphicsView(self.scene, self)
            return
        self.__text__ = self.text[0:-2]
        QGraphicsView(self.scene, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())