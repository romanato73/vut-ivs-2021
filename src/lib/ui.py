# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# ########################################
# Brief: View made in QtDesigner -> autogenerated file + manual input
# Project: Calculator
# File: ui.py
# Authors: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#          Roman Országh <xorsza01(at)fit.vutbr.cz>
#          Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
# 	       Vlk Jakub <xvlkja07(at)fit.vutbr.cz>
# ########################################

from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ivsmath(object):
    def setupUi(self, ivsmath):
        ivsmath.setObjectName("ivsmath")
        ivsmath.setFixedSize(400, 550)
        # Added fonts
        QtGui.QFontDatabase.addApplicationFont('assets/FontAwesome-5-Solid.otf')
        QtGui.QFontDatabase.addApplicationFont('assets/Nunito-Black.ttf')
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        ivsmath.setFont(font)
        # Added styles
        with open("assets/master.qss", "r") as file:
            ivsmath.setStyleSheet(file.read())
        self.gridWidget = QtWidgets.QWidget(ivsmath)
        self.gridWidget.setGeometry(QtCore.QRect(0, 150, 400, 400))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_comma = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_comma.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_comma.sizePolicy().hasHeightForWidth())
        self.pushButton_comma.setSizePolicy(sizePolicy)
        self.pushButton_comma.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_comma.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_comma.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        self.pushButton_comma.setFont(font)
        self.pushButton_comma.setObjectName("pushButton_comma")
        self.gridLayout.addWidget(self.pushButton_comma, 6, 3, 1, 1)
        self.pushButton_pi = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_pi.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pi.sizePolicy().hasHeightForWidth())
        self.pushButton_pi.setSizePolicy(sizePolicy)
        self.pushButton_pi.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_pi.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_pi.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        self.pushButton_pi.setFont(font)
        self.pushButton_pi.setObjectName("pushButton_pi")
        self.gridLayout.addWidget(self.pushButton_pi, 1, 3, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_clear.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_clear.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_clear.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 0, 4, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_1.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_1.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 5, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_7.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_7.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_sin = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_sin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sin.sizePolicy().hasHeightForWidth())
        self.pushButton_sin.setSizePolicy(sizePolicy)
        self.pushButton_sin.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_sin.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_sin.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.gridLayout.addWidget(self.pushButton_sin, 0, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_div.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        self.pushButton_div.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_div.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_div.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_8.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_8.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_3.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 3, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_eq.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eq.sizePolicy().hasHeightForWidth())
        self.pushButton_eq.setSizePolicy(sizePolicy)
        self.pushButton_eq.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_eq.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_eq.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 6, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_2.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_5.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_4.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_4.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_pow = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_pow.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pow.sizePolicy().hasHeightForWidth())
        self.pushButton_pow.setSizePolicy(sizePolicy)
        self.pushButton_pow.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_pow.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_pow.setBaseSize(QtCore.QSize(40, 40))
        sqrtIcon = QtGui.QPixmap('assets/xn.png')
        self.pushButton_pow.setIcon(QtGui.QIcon(sqrtIcon))
        self.pushButton_pow.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.gridLayout.addWidget(self.pushButton_pow, 1, 0, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_0.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_0.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 6, 1, 1, 1)
        self.pushButton_fact = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_fact.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fact.sizePolicy().hasHeightForWidth())
        self.pushButton_fact.setSizePolicy(sizePolicy)
        self.pushButton_fact.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_fact.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_fact.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        self.pushButton_fact.setFont(font)
        self.pushButton_fact.setObjectName("pushButton_fact")
        self.gridLayout.addWidget(self.pushButton_fact, 6, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_9.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_9.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 3, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_sub.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_sub.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_sub.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 4, 4, 1, 1)
        self.pushButton_cos = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_cos.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cos.sizePolicy().hasHeightForWidth())
        self.pushButton_cos.setSizePolicy(sizePolicy)
        self.pushButton_cos.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_cos.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_cos.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setText("cos")
        self.pushButton_cos.setCheckable(False)
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.gridLayout.addWidget(self.pushButton_cos, 0, 0, 1, 1)
        self.pushButton_del = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_del.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_del.sizePolicy().hasHeightForWidth())
        self.pushButton_del.setSizePolicy(sizePolicy)
        self.pushButton_del.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_del.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_del.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.gridLayout.addWidget(self.pushButton_del, 0, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_6.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_6.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(25)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 3, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_mul.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_mul.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_mul.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 4, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_sqrt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sqrt.sizePolicy().hasHeightForWidth())
        self.pushButton_sqrt.setSizePolicy(sizePolicy)
        self.pushButton_sqrt.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_sqrt.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_sqrt.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Black")
        font.setPointSize(15)
        self.pushButton_sqrt.setFont(font)
        sqrtIcon = QtGui.QPixmap('assets/sqrt.png')
        self.pushButton_sqrt.setIcon(QtGui.QIcon(sqrtIcon))
        self.pushButton_sqrt.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 1, 1, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.gridWidget)
        self.pushButton_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_add.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_add.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Solid")
        font.setPointSize(15)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 5, 4, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(ivsmath)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 400, 150))
        self.graphicsView.setObjectName("graphicsView")

        ########################################
        self.display = QtWidgets.QLineEdit(ivsmath)
        self.display.setFixedHeight(100)
        self.display.setFixedWidth(400)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.display.setAttribute(Qt.WA_MacShowFocusRect, False)  # MacOS fix blue border
        self.display.setFocus()
        self.display.move(0, 25)
        self.display.setObjectName("display")
        # Regex
        regex = QtCore.QRegExp("(sin\(|cos\(|[0-9\/*--+,√^π!\(\)])+")
        validator = QtGui.QRegExpValidator(regex)
        self.display.setValidator(validator)
        ########################################

        self.retranslateUi(ivsmath)
        QtCore.QMetaObject.connectSlotsByName(ivsmath)
        ivsmath.setTabOrder(self.graphicsView, self.pushButton_7)
        ivsmath.setTabOrder(self.pushButton_7, self.pushButton_8)
        ivsmath.setTabOrder(self.pushButton_8, self.pushButton_9)
        ivsmath.setTabOrder(self.pushButton_9, self.pushButton_5)
        ivsmath.setTabOrder(self.pushButton_5, self.pushButton_4)
        ivsmath.setTabOrder(self.pushButton_4, self.pushButton_6)
        ivsmath.setTabOrder(self.pushButton_6, self.pushButton_1)
        ivsmath.setTabOrder(self.pushButton_1, self.pushButton_2)
        ivsmath.setTabOrder(self.pushButton_2, self.pushButton_3)
        ivsmath.setTabOrder(self.pushButton_3, self.pushButton_comma)
        ivsmath.setTabOrder(self.pushButton_comma, self.pushButton_clear)
        ivsmath.setTabOrder(self.pushButton_clear, self.pushButton_add)
        ivsmath.setTabOrder(self.pushButton_add, self.pushButton_sub)
        ivsmath.setTabOrder(self.pushButton_sub, self.pushButton_pow)
        ivsmath.setTabOrder(self.pushButton_pow, self.pushButton_sqrt)
        ivsmath.setTabOrder(self.pushButton_sqrt, self.pushButton_pi)
        ivsmath.setTabOrder(self.pushButton_pi, self.pushButton_div)
        ivsmath.setTabOrder(self.pushButton_div, self.pushButton_cos)
        ivsmath.setTabOrder(self.pushButton_cos, self.pushButton_del)
        ivsmath.setTabOrder(self.pushButton_del, self.pushButton_eq)
        ivsmath.setTabOrder(self.pushButton_eq, self.pushButton_mul)
        ivsmath.setTabOrder(self.pushButton_mul, self.pushButton_sin)

    def retranslateUi(self, ivsmath):
        _translate = QtCore.QCoreApplication.translate
        ivsmath.setWindowTitle(_translate("ivsmath", "CalcStuck"))
        ivsmath.setWindowIcon(QtGui.QIcon('assets/logo.png'))
        self.pushButton_comma.setText(_translate("ivsmath", ","))
        self.pushButton_pi.setText(_translate("ivsmath", "π"))
        self.pushButton_clear.setText(_translate("ivsmath", "C"))
        self.pushButton_1.setText(_translate("ivsmath", "1"))
        self.pushButton_7.setText(_translate("ivsmath", "7"))
        self.pushButton_sin.setText(_translate("ivsmath", "sin"))
        self.pushButton_div.setText(_translate("ivsmath", ""))
        self.pushButton_8.setText(_translate("ivsmath", "8"))
        self.pushButton_3.setText(_translate("ivsmath", "3"))
        self.pushButton_eq.setText(_translate("ivsmath", ""))
        self.pushButton_2.setText(_translate("ivsmath", "2"))
        self.pushButton_5.setText(_translate("ivsmath", "5"))
        self.pushButton_4.setText(_translate("ivsmath", "4"))
        self.pushButton_pow.setText(_translate("ivsmath", ""))
        self.pushButton_0.setText(_translate("ivsmath", "0"))
        self.pushButton_fact.setText(_translate("ivsmath", "!"))
        self.pushButton_9.setText(_translate("ivsmath", "9"))
        self.pushButton_sub.setText(_translate("ivsmath", ""))
        self.pushButton_del.setText(_translate("ivsmath", ""))
        self.pushButton_6.setText(_translate("ivsmath", "6"))
        self.pushButton_mul.setText(_translate("ivsmath", ""))
        self.pushButton_sqrt.setText(_translate("ivsmath", ""))
        self.pushButton_add.setText(_translate("ivsmath", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ivsmath = QtWidgets.QWidget()
    ui = Ui_ivsmath()
    ui.setupUi(ivsmath)
    ivsmath.show()
    sys.exit(app.exec_())
