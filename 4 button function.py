import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Application Structure")
        self.setWindowIcon(QtGui.QIcon('star.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        self.show()

    def close_application(self):
        print("whoaaaa so custom !!!")
        sys.exit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())