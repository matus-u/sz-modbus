from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.DevicesConfiguration import Ui_DevicesConfiguration
from ui import AddEditDeviceWindow
from ui import Helpers
from model import ModbusDeviceDict

class DevicesConfigurationWidget(QtWidgets.QWidget):

    def __init__(self, configuration):
        super(DevicesConfigurationWidget, self).__init__()
        self.ui = Ui_DevicesConfiguration()
        self.ui.setupUi(self)
        self.ui.addDeviceButton.clicked.connect(self.onAddButton)
        self.configuration = configuration

    def onAddButton(self):
        w = AddEditDeviceWindow.AddEditDeviceWindow(self)
        w.finished.connect(lambda retCode: self.onAddFinished(w, retCode))
        Helpers.openSubWindow(self, w)

    def onAddFinished(self, window, code):
        if code:
            self.configuration.append(window.deviceConf())
            self.ui.devicesWidget.insertRow(self.ui.devicesWidget.rowCount())
            rowNumber = self.ui.devicesWidget.rowCount()
            self.ui.devicesWidget.setItem(rowNumber-1 , 0, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.NAME]))
            self.ui.devicesWidget.setItem(rowNumber-1 , 1, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE]))
            self.ui.devicesWidget.setItem(rowNumber-1 , 2, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.ADDRESS]))

    def onDeleteButton(self):
        pass

    def onEditButton(self):
        pass

    def onApplyButton(self):
        pass

    def onBackButton(self):
        pass

