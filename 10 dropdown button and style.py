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

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 200)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

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