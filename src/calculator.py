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
        self.scene.addText(self.__text__, self.deffont, )
        gpv = QGraphicsView(self.scene, self)
        gpv.setMinimumWidth(400)
        gpv.setAlignment(Qt.AlignLeft)

        self.Button()
        self.ui.pushButton_1.clicked.connect(self.button_1)
        self.ui.pushButton_2.clicked.connect(self.button_2)
        self.ui.pushButton_3.clicked.connect(self.button_3)
        self.ui.pushButton_4.clicked.connect(self.button_4)
        self.ui.pushButton_5.clicked.connect(self.button_5)
        self.ui.pushButton_6.clicked.connect(self.button_6)
        self.ui.pushButton_7.clicked.connect(self.button_7)
        self.ui.pushButton_8.clicked.connect(self.button_8)
        self.ui.pushButton_9.clicked.connect(self.button_9)
        self.ui.pushButton_0.clicked.connect(self.button_0)
        self.ui.pushButton_add.clicked.connect(self.button_add)
        self.ui.pushButton_sub.clicked.connect(self.button_sub)
        self.ui.pushButton_div.clicked.connect(self.button_div)
        self.ui.pushButton_clear.clicked.connect(self.button_clear)
        self.ui.pushButton_del.clicked.connect(self.button_del)
        self.ui.pushButton_sin.clicked.connect(self.button_sin)
        self.ui.pushButton_cos.clicked.connect(self.button_cos)
        self.ui.pushButton_fact.clicked.connect(self.button_fact)
        self.ui.pushButton_sqrt.clicked.connect(self.button_sqrt)
        self.ui.pushButton_pow.clicked.connect(self.button_pow)
        self.ui.pushButton_pi.clicked.connect(self.button_pi)
        self.ui.pushButton_eq.clicked.connect(self.button_eq)
        self.ui.pushButton_comma.clicked.connect(self.button_decimal)

        self.scene.clear()
        self.scene.addText(self.__text__, self.deffont)

    def button_1(self):
        pass

    def button_2(self):
        pass

    def button_3(self):
        pass

    def button_4(self):
        pass

    def button_5(self):
        pass

    def button_6(self):
        pass

    def button_7(self):
        pass

    def button_8(self):
        pass

    def button_9(self):
        pass

    def button_0(self):
        pass

    def button_add(self):
        pass

    def button_sub(self):
        pass

    def button_div(self):
        pass

    def button_mul(self):
        pass

    def button_sin(self):
        pass

    def button_cos(self):
        pass

    def button_del(self):
        pass

    def button_clear(self):
        pass

    def button_pi(self):
        pass

    def button_sqrt(self):
        pass

    def button_fact(self):
        pass

    def button_decimal(self):
        pass

    def button_pow(self):
        pass

    def button_eq(self):
        pass

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

    def appendText(self, str: str):
        self.__text__ += str

    def clearText(self):
        self.__text__ = ""

    def delText(self):
        if len(self.__text__) == 0:
            return
        if len(self.__text__) == 1:
            self.clearText()
            return
        self.__text__ = self.__text__[0:-1]

    def parseText(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
