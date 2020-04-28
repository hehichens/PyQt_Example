import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800, 450)
    w.move(300, 300)
    w.setWindowTitle("Hello, World")
    w.show()
    sys.exit(app.exec_())
    