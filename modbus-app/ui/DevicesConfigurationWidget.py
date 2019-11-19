from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.DevicesConfiguration import Ui_DevicesConfiguration

class DevicesConfigurationWidget(QtWidgets.QWidget):

    def __init__(self):
        super(DevicesConfigurationWidget, self).__init__()

        self.ui = Ui_DevicesConfiguration()
        self.ui.setupUi(self)

