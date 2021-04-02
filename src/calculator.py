import sys
from ui import Ui_ivsmath
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem , QLineEdit
from PyQt5.QtGui import QPen, QBrush, QFont, QColor, QTextCharFormat
from PyQt5.Qt import Qt, QColor, pyqtSlot
import asyncio
import time
from PyQt5.QtCore import QTimer


class CalculatorWindow(QWidget):
    def __init__(self):
        super(CalculatorWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ivsmath()
        self.ui.setupUi(self)

        self.changed_by_click = False
        self.__text = ''

        transparentcolor = QColor()
        #transparentcolor.setAlpha(0)
        transparentcolor.cyan()
        # pen = QPen()
        # pen.setColor(transparentcolor)

        self.deffont = QFont("Sans Serif")
        self.deffont.setPixelSize(50)
        self.deffont.setFamily("Sans Serif")

        textformat = QTextCharFormat()
        textformat.setFont(self.deffont)

        self.__fading_button = None
        self.__fading_button = ''  # contains string on display

        self.ui.display.textChanged.connect(self.user_input)
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
        self.ui.pushButton_mul.clicked.connect(self.button_mul)
        self.ui.pushButton_clear.clicked.connect(self.button_clear)
        self.ui.pushButton_del.clicked.connect(self.button_del)
        self.ui.pushButton_sin.clicked.connect(self.button_sin)
        self.ui.pushButton_cos.clicked.connect(self.button_cos)
        # nutno pridat tlacitko pro fact, a dat pryc +-
        #self.ui.pushButton_fact.clicked.connect(self.button_fact)
        self.ui.pushButton_sqrt.clicked.connect(self.button_sqrt)
        self.ui.pushButton_pow.clicked.connect(self.button_pow)
        self.ui.pushButton_pi.clicked.connect(self.button_pi)
        self.ui.pushButton_eq.clicked.connect(self.button_eq)
        self.ui.pushButton_comma.clicked.connect(self.button_decimal)
        # self.scene.clear()
        # self.scene.addText(self.__text, self.deffont)

    @pyqtSlot()
    def fade(self):
        #a = self.findChild(QWidget, self.sender().objectName()) -- takto sa dá tiež získať meno toho sendera XD
        fading_button = self.sender()
        fading_button.setWindowOpacity(0.5)
        fading_button.setStyleSheet("background-color: #1a1a1a")
        QTimer.singleShot(75, lambda: self.unfade(fading_button))

    @pyqtSlot()
    def unfade(self, fading_button):
        fading_button.setWindowOpacity(1)
        fading_button.setStyleSheet("")

    @pyqtSlot(str)
    def user_input(self, edited_text):
        if not self.changed_by_click:
            #print(edited_text)
            self.fade_through_edit(self.check_edit(edited_text))
        else:
            self.changed_by_click = False
        self.__text = edited_text  # get text
        print('---' + self.__text)

    def fade_through_edit(self, button):
        if not button:  # button click also invokes signal Changed but we do not want this fade to do anything then
            return
        button.setWindowOpacity(0.5)
        button.setStyleSheet("background-color: #1a1a1a")
        QTimer.singleShot(75, lambda: self.unfade(button))

    def check_edit(self, text):
        if (text.__len__()-1) > self.__text.__len__():
            return False  # in case more than 1 char was inserted at once do not fade
        if text.__len__() < self.__text.__len__():
            return self.ui.pushButton_del  # case more than 1 char was removed
        print("here")
        for i in range(text.__len__()):
            try:
                if text[i] != self.__text[i]:
                    return self.char_fsm(text[i])
            except IndexError:
                return self.char_fsm(text[-1])

    def char_fsm(self, char):  # finite state machine looking at char
        if char == '1':
            return self.ui.pushButton_1
        elif char == '2':
            return self.ui.pushButton_2
        elif char == '3':
            return self.ui.pushButton_3
        elif char == '4':
            return self.ui.pushButton_4
        elif char == '5':
            return self.ui.pushButton_5
        elif char == '6':
            return self.ui.pushButton_6
        elif char == '7':
            return self.ui.pushButton_7
        elif char == '8':
            return self.ui.pushButton_8
        elif char == '9':
            return self.ui.pushButton_9
        elif char == '0':
            return self.ui.pushButton_0
        elif char == '+':
            return self.ui.pushButton_add
        elif char == '-':
            return self.ui.pushButton_sub
        elif char == '*':
            return self.ui.pushButton_mul
        elif char == '/':
            return self.ui.pushButton_div
        elif char == '√':
            return self.ui.pushButton_sqrt
        elif char == ',':
            return self.ui.pushButton_comma
        elif char == '^':
            return self.ui.pushButton_pow
        elif char == '^':
            return self.ui.pushButton_pow
        elif char == 'π':
            return self.ui.pushButton_pi
        else:  # invalid character
            return False


        # elif char == '!':
        #     return self.ui.pushButton_fact



    def renderText(self):
        self.ui.display.setText(self.__text)
        self.ui.display.setFocus()
        self.__fading_button = self.sender()

    def button_1(self):
        self.changed_by_click = True
        self.ui.display.insert('1')
        self.ui.display.setFocus()
        self.fade()

    def button_2(self):
        self.changed_by_click = True
        self.ui.display.insert('2')
        self.ui.display.setFocus()
        self.fade()

    def button_3(self):
        self.changed_by_click = True
        self.ui.display.insert('3')
        self.ui.display.setFocus()
        self.fade()

    def button_4(self):
        self.changed_by_click = True
        self.ui.display.insert('4')
        self.ui.display.setFocus()
        self.fade()

    def button_5(self):
        self.changed_by_click = True
        self.ui.display.insert('5')
        self.ui.display.setFocus()
        self.fade()

    def button_6(self):
        self.changed_by_click = True
        self.ui.display.insert('6')
        self.ui.display.setFocus()
        self.fade()

    def button_7(self):
        self.changed_by_click = True
        self.ui.display.insert('7')
        self.ui.display.setFocus()
        self.fade()

    def button_8(self):
        self.changed_by_click = True
        self.ui.display.insert('8')
        self.ui.display.setFocus()
        self.fade()

    def button_9(self):
        self.changed_by_click = True
        self.ui.display.insert('9')
        self.ui.display.setFocus()
        self.fade()

    def button_0(self):
        self.changed_by_click = True
        self.ui.display.insert('0')
        self.ui.display.setFocus()
        self.fade()

    def button_add(self):
        self.changed_by_click = True
        self.ui.display.insert('+')
        self.ui.display.setFocus()
        self.fade()

    def button_sub(self):
        self.changed_by_click = True
        self.ui.display.insert('-')
        self.ui.display.setFocus()
        self.fade()

    def button_div(self):
        self.changed_by_click = True
        self.ui.display.insert('/')
        self.ui.display.setFocus()
        self.fade()

    def button_mul(self):
        self.changed_by_click = True
        self.ui.display.insert('*')
        self.ui.display.setFocus()
        self.fade()

    def button_sin(self):
        self.changed_by_click = True
        self.ui.display.insert('sin(')
        self.ui.display.setFocus()
        self.fade()

    def button_cos(self):
        self.changed_by_click = True
        self.ui.display.insert('cos(')
        self.ui.display.setFocus()
        self.fade()

    def button_del(self):
        self.changed_by_click = True
        self.ui.display.backspace()
        self.ui.display.setFocus()
        self.fade()
        pass

    def button_clear(self):
        #self.delText()
        self.changed_by_click = True
        self.clearText()
        self.ui.display.setText(self.__text)
        self.ui.display.setFocus()
        self.fade()

    def button_pi(self):
        #self.appendText("π")
        self.changed_by_click = True
        self.ui.display.insert('π')
        self.ui.display.setFocus()
        self.fade()

    def button_sqrt(self):
        #self.appendText("√")
        self.changed_by_click = True
        self.ui.display.insert('√')
        self.ui.display.setFocus()
        self.fade()

    def button_fact(self):
        self.changed_by_click = True
        self.ui.display.insert('!')
        self.ui.display.setFocus()
        self.fade()

    def button_decimal(self):
        self.changed_by_click = True
        self.ui.display.insert(',')
        self.ui.display.setFocus()
        self.fade()

    def button_pow(self):
        self.changed_by_click = True
        self.ui.display.insert('^')
        self.ui.display.setFocus()
        self.fade()

    def button_eq(self):
        # todo
        self.fade()
        #self.renderText()
        pass

    __text = ""
    def keyPressEvent(self, event):
        # if event.key() == Qt.Key_1:
        #     self.ui.pushButton_1.click()
        #     return
        # if event.key() == Qt.Key_2:
        #     self.ui.pushButton_2.click()
        #     return
        # if event.key() == Qt.Key_3:
        #     self.ui.pushButton_3.click()
        #     return
        # if event.key() == Qt.Key_4:
        #     self.ui.pushButton_4.click()
        #     return
        # if event.key() == Qt.Key_5:
        #     self.ui.pushButton_5.click()
        #     return
        # if event.key() == Qt.Key_6:
        #     self.ui.pushButton_6.click()
        #     return
        # if event.key() == Qt.Key_7:
        #     self.ui.pushButton_7.click()
        #     return
        # if event.key() == Qt.Key_8:
        #     self.ui.pushButton_8.click()
        #     return
        # if event.key() == Qt.Key_9:
        #     self.ui.pushButton_9.click()
        #     return
        # if event.key() == Qt.Key_0:
        #     self.ui.pushButton_0.click()
        #     return
        # if event.key() == Qt.Key_Backspace:
        #     self.ui.pushButton_del.click()
        #     return
        # if (event.key() == Qt.Key_Delete) or (event.key() == Qt.Key_C):
        #     self.ui.pushButton_clear.click()
        #     return
        # if (event.key() == Qt.Key_Comma or event.key() == Qt.Key_Period):
        #     self.ui.pushButton_comma.click()
        #     return
        # if event.key() == Qt.Key_Plus:
        #     self.ui.pushButton_add.click()
        #     return
        # if event.key() == Qt.Key_Minus:
        #     self.ui.pushButton_sub.click()
        #     return
        # if event.key() == Qt.Key_Slash:
        #     self.ui.pushButton_div.click()
        #     return
        # if event.key() == Qt.Key_Asterisk:
        #     self.ui.pushButton_mul.click()
        #     return
        if event.key() == Qt.Key_Enter:   # tento nie je predefinovany -> funguje to normalne (faduje)
            self.ui.pushButton_eq.click()
            return


        # self.scene.clear()
        # self.scene.addText(self.__text, self.deffont)
       # print(self.__text)

    def appendText(self, str: str):
        self.__text += str

    def clearText(self):
        self.__text = ""

    def delText(self):
        if len(self.__text) == 0:
            return
        if len(self.__text) == 1:
            self.clearText()
            return
        self.__text = self.__text[0:-1]

    def parseText(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
