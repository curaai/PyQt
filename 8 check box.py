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

        checkBox = QtGui.QCheckBox("Enlarge Windows", self)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.move(100, 25)
        
        self.show()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(70, 50, 1000, 600)
        else:
            self.setGeometry(70, 50, 500, 300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Extract!",
                                            "Get Into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaaaaooooooooow!!!!")
            sys.exit()
        else:
            pass



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())