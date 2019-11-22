from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.AddEditDevice import Ui_AddEditDevice

from model.ModbusDeviceDict import DeviceDictAccessor
from model.ModbusDeviceType import DeviceTypes

class AddEditDeviceWindow(QtWidgets.QDialog):

    def __init__(self, parent):
        super(AddEditDeviceWindow, self).__init__(parent)
        self.ui = Ui_AddEditDevice()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.deviceTypeModel = QtCore.QStringListModel(DeviceTypes.getTypes())
        self.ui.deviceTypeComboBox.setModel(self.ui.deviceTypeModel)

    def deviceConf(self):
        return DeviceDictAccessor.createDict(self.ui.deviceNameEdit.text(), self.ui.deviceAddress.text(), self.ui.deviceTypeComboBox.currentText())

    def setDeviceConfData(self, config):
        self.ui.deviceNameEdit.setText(config[DeviceDictAccessor.NAME])
        self.ui.deviceAddress.setValue(int(config[DeviceDictAccessor.ADDRESS]))
        self.ui.deviceTypeComboBox.setCurrentIndex(DeviceTypes.getTypes().index(config[DeviceDictAccessor.DEV_TYPE]))

    def paintEvent(self, event=None):
        painter = QtGui.QPainter(self)
        painter.setOpacity(0.7)
        painter.setBrush(QtCore.Qt.white)
        painter.setPen(QtGui.QPen(QtCore.Qt.white))
        painter.drawRect(self.rect())

