"""
Main
"""
from GUI import *
import sys

App = QApplication(sys.argv)

window = GUI()

window.show()

sys.exit(App.exec_())
