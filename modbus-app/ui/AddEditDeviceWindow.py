from PyQt5 import QtCore
from PyQt5 import QtWidgets
from generated.AddEditDevice import Ui_AddEditDevice

from model.ModbusDeviceDict import DeviceDictAccessor
from model.ModbusDeviceType import DeviceTypes

from ui import Helpers

class AddEditDeviceWindow(Helpers.TransparentDialog):

    def __init__(self, parent, editMode = False, notAllowedAddresses = []):
        super(AddEditDeviceWindow, self).__init__(parent)
        self.ui = Ui_AddEditDevice()
        self.ui.setupUi(self)
        if editMode:
            self.ui.deviceTypeComboBox.setEnabled(False)

        self.notAllowedAddresses = notAllowedAddresses
        self.ui.deviceTypeModel = QtCore.QStringListModel(DeviceTypes.getTypes())
        self.ui.deviceTypeComboBox.setModel(self.ui.deviceTypeModel)
        self.ui.okButton.clicked.connect(self.onOkButton)

    def deviceConf(self):
        return DeviceDictAccessor.createDict(self.ui.deviceNameEdit.text(), self.ui.deviceAddress.text(), self.ui.deviceTypeComboBox.currentText())

    def setDeviceConfData(self, config):
        self.ui.deviceNameEdit.setText(config[DeviceDictAccessor.NAME])
        self.ui.deviceAddress.setValue(int(config[DeviceDictAccessor.ADDRESS]))
        self.ui.deviceTypeComboBox.setCurrentIndex(DeviceTypes.getTypes().index(config[DeviceDictAccessor.DEV_TYPE]))

    def onOkButton(self):
        if self.ui.deviceAddress.value() == 0:
            QtWidgets.QMessageBox.warning(self, self.tr("Wrong address"), self.tr("It is not allowed to set 0 as address value."))
            return

        if self.ui.deviceNameEdit.text() == "":
            QtWidgets.QMessageBox.warning(self, self.tr("Wrong name"), self.tr("Empty name is not allowed."))
            return

        if str(self.ui.deviceAddress.value()) in self.notAllowedAddresses:
            QtWidgets.QMessageBox.warning(self, self.tr("Wrong address"), self.tr("Address is already used by another device."))
            return

        self.accept()
