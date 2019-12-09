from PyQt5 import QtCore
from generated.AddEditDevice import Ui_AddEditDevice

from model.ModbusDeviceDict import DeviceDictAccessor
from model.ModbusDeviceType import DeviceTypes

from ui import Helpers

class AddEditDeviceWindow(Helpers.TransparentDialog):

    def __init__(self, parent, editMode = False):
        super(AddEditDeviceWindow, self).__init__(parent)
        self.ui = Ui_AddEditDevice()
        self.ui.setupUi(self)
        if editMode:
            self.ui.deviceTypeComboBox.setEnabled(False)

        self.ui.deviceTypeModel = QtCore.QStringListModel(DeviceTypes.getTypes())
        self.ui.deviceTypeComboBox.setModel(self.ui.deviceTypeModel)

    def deviceConf(self):
        return DeviceDictAccessor.createDict(self.ui.deviceNameEdit.text(), self.ui.deviceAddress.text(), self.ui.deviceTypeComboBox.currentText())

    def setDeviceConfData(self, config):
        self.ui.deviceNameEdit.setText(config[DeviceDictAccessor.NAME])
        self.ui.deviceAddress.setValue(int(config[DeviceDictAccessor.ADDRESS]))
        self.ui.deviceTypeComboBox.setCurrentIndex(DeviceTypes.getTypes().index(config[DeviceDictAccessor.DEV_TYPE]))
