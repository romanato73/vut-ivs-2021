import sys
import os

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Mathstuckgui(QWidget):
    def __int__(self):
        super(Mathstuckgui, self).__init__()
        Mathstuckgui.loadUi('form.ui', self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = Mathstuckgui()
    widget.show()
    sys.exit(app.exec_())
