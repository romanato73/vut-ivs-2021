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

        transparentcolor = QColor()
        transparentcolor.setAlpha(0)
        # pen = QPen()
        # pen.setColor(transparentcolor)


        self.deffont = QFont("Sans Serif")
        self.deffont.setPixelSize(20)
        self.deffont.setFamily("Sans Serif")

        textformat = QTextCharFormat()
        textformat.setFont(self.deffont)
        # textformat.setTextOutline(pen)

        self.scene = QGraphicsScene()

        self.scene.setBackgroundBrush(transparentcolor)
        self.scene.addText(self.__text__ , self.deffont, )
        gpv = QGraphicsView(self.scene, self)
        gpv.setMinimumWidth(400)
        gpv.setAlignment(Qt.AlignLeft)

        self.ui.pushButton_1.clicked.connect(lambda: self.appendText('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.appendText('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.appendText('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.appendText('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.appendText('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.appendText('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.appendText('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.appendText('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.appendText('9'))
        self.ui.pushButton_0.clicked.connect(lambda: self.appendText('0'))
        self.ui.pushButton_add.clicked.connect(lambda: self.appendText('+'))
        self.ui.pushButton_sub.clicked.connect(lambda: self.appendText('-'))
        self.ui.pushButton_div.clicked.connect(lambda: self.appendText('*'))
        self.ui.pushButton_mul.clicked.connect(lambda: self.appendText('/'))




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
        if event.key() == Qt.Key_Backspace:
            self.delText()
        # Nevím jestl je dobrý nápad tady dávat i to delete
        if (event.key() == Qt.Key_Delete) or (event.key() == Qt.Key_C):
            self.clearText()
        if (event.key() == Qt.Key_Comma):
            # desetiná tečka nevím jak se jmenuje key
            self.appendText(",")
        if event.key() == Qt.Key_Plus:
            self.appendText("+")
        if event.key() == Qt.Key_Minus:
            self.appendText("-")
        if event.key() == Qt.Key_Slash:
            self.appendText("/")
        if event.key() == Qt.Key_Asterisk:
            self.appendText("*")
        if event.key() == Qt.Key_Enter:
            self.parseText()

        self.scene.clear()
        self.scene.addText(self.__text__, self.deffont)
        print(self.__text__)


    def appendText(self, str:str, sep=''):
        self.__text__ += str
        self.scene.clear()
        self.scene.addText(self.__text__, self.deffont)

    def clearText(self):
        self.__text__ = ""
        self.scene.clear()
        self.scene.addText(self.__text__, self.deffont)

    def delText(self):
        if len(self.__text__) == 0:
            return
        if len(self.__text__) == 1:
            self.clearText()
            return
        self.__text__ = self.__text__[0:-1]
        self.scene.clear()
        self.scene.addText(self.__text__, self.deffont)

    def parseText(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())