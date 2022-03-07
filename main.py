from src.gui import Gui
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Gui()
    window.show()

    app.exec()
