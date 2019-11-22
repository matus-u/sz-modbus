from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.DevicesConfiguration import Ui_DevicesConfiguration
from ui import AddEditDeviceWindow
from ui import Helpers
from model import ModbusDeviceDict

class DevicesConfigurationWindow(QtWidgets.QDialog):

    def __init__(self, parent, configuration):
        super(DevicesConfigurationWindow, self).__init__(parent)
        self.ui = Ui_DevicesConfiguration()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.ui.addDeviceButton.clicked.connect(self.onAddButton)
        self.ui.removeDeviceButton.clicked.connect(self.onRemoveButton)
        self.ui.editDeviceButton.clicked.connect(self.onEditButton)
        self.configuration = configuration
        self.ui.devicesWidget.itemSelectionChanged.connect(self.onSelectionChanged)
        self.ui.devicesWidget.resizeColumnsToContents()

        self.ui.removeDeviceButton.setEnabled(False)
        self.ui.editDeviceButton.setEnabled(False)

        self.populateConfiguration()

    def populateConfiguration(self):
        self.ui.devicesWidget.setRowCount(len(self.configuration))
        for index, item in enumerate(self.configuration):
            self.ui.devicesWidget.setItem(index , 0, QtWidgets.QTableWidgetItem(item[ModbusDeviceDict.DeviceDictAccessor.NAME]))
            self.ui.devicesWidget.setItem(index , 1, QtWidgets.QTableWidgetItem(item[ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE]))
            self.ui.devicesWidget.setItem(index , 2, QtWidgets.QTableWidgetItem(item[ModbusDeviceDict.DeviceDictAccessor.ADDRESS]))

    def onAddButton(self):
        w = AddEditDeviceWindow.AddEditDeviceWindow(self)
        w.finished.connect(lambda retCode: self.onAddFinished(w, retCode))
        Helpers.openSubWindow(self, w)
        w.move(self.pos().x(), self.pos().y())

    def onAddFinished(self, window, code):
        if code:
            self.configuration.append(window.deviceConf())
            self.ui.devicesWidget.insertRow(self.ui.devicesWidget.rowCount())
            rowNumber = self.ui.devicesWidget.rowCount()
            self.ui.devicesWidget.setItem(rowNumber-1 , 0, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.NAME]))
            self.ui.devicesWidget.setItem(rowNumber-1 , 1, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE]))
            self.ui.devicesWidget.setItem(rowNumber-1 , 2, QtWidgets.QTableWidgetItem(self.configuration[rowNumber-1][ModbusDeviceDict.DeviceDictAccessor.ADDRESS]))

    def onSelectionChanged(self):
        if not self.ui.devicesWidget.selectedItems():
            self.ui.removeDeviceButton.setEnabled(False)
            self.ui.editDeviceButton.setEnabled(False)
        else:
            self.ui.removeDeviceButton.setEnabled(True)
            self.ui.editDeviceButton.setEnabled(True)

    def onRemoveButton(self):
        index = self.ui.devicesWidget.currentRow()
        self.configuration.pop(index)
        self.ui.devicesWidget.removeRow(index)

    def onEditButton(self):
        w = AddEditDeviceWindow.AddEditDeviceWindow(self)
        index = self.ui.devicesWidget.currentRow()
        w.setDeviceConfData(self.configuration[index])
        w.finished.connect(lambda retCode: self.onEditFinished(w, retCode, index))
        Helpers.openSubWindow(self, w)
        w.move(self.pos().x(), self.pos().y())

    def onEditFinished(self, window, code, index):
        if code:
            self.configuration[index] = window.deviceConf()
            self.ui.devicesWidget.setItem(index , 0, QtWidgets.QTableWidgetItem(self.configuration[index][ModbusDeviceDict.DeviceDictAccessor.NAME]))
            self.ui.devicesWidget.setItem(index , 1, QtWidgets.QTableWidgetItem(self.configuration[index][ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE]))
            self.ui.devicesWidget.setItem(index , 2, QtWidgets.QTableWidgetItem(self.configuration[index][ModbusDeviceDict.DeviceDictAccessor.ADDRESS]))


    def getConfiguration(self):
        return self.configuration

