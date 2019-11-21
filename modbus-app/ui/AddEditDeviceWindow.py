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

        self.ui.deviceTypeModel = QtCore.QStringListModel(DeviceTypes.getTypes())
        self.ui.deviceTypeComboBox.setModel(self.ui.deviceTypeModel)

    def deviceConf(self):
        return DeviceDictAccessor.createDict(self.ui.deviceNameEdit.text(), self.ui.deviceAddress.text(), self.ui.deviceTypeComboBox.currentText())

