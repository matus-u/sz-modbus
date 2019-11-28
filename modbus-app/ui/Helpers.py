from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

def openSubWindow(parent, window):
    window.show()
    window.raise_()
    window.activateWindow()
#    window.move(window.pos().x(), parent.pos().y() + 60)


class TransparentDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(TransparentDialog, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def paintEvent(self, event=None):
        painter = QtGui.QPainter(self)
        painter.setOpacity(0.7)
        painter.setBrush(QtCore.Qt.white)
        painter.setPen(QtGui.QPen(QtCore.Qt.white))
        painter.drawRect(self.rect())
