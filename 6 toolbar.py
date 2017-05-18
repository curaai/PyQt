import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Application Structure")
        self.setWindowIcon(QtGui.QIcon('star.png'))

        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        extractAction = QtGui.QAction(QtGui.QIcon('star.png'), "Flee the Scene", self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)

        self.show()

    def close_application(self):
        print("whoaaaa so custom !!!")
        sys.exit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())