import sys
import ui
from PyQt5 import QtWidgets

# Initialize Application
app = QtWidgets.QApplication(sys.argv)

# Create calculator widget
calculator = QtWidgets.QWidget()

# Interface instance
interface = ui.Ui_ivsmath()

# Setup interface with calculator
interface.setupUi(calculator)

# Show calculator
calculator.show()

# Terminate application
sys.exit(app.exec_())
