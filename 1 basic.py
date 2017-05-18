import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

windows = QtGui.QWidget()
windows.setGeometry(50, 50, 500, 300)
windows.setWindowTitle('PyQt Tutos')

windows.show()