from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class DevicesSettings(QtCore.QObject):
    SettingsPath = "configs/devices.conf"
    SettingsFormat = QtCore.QSettings.NativeFormat

    DevicesString = "Devices"

    def __init__(self):
        super().__init__()

        self.settings = QtCore.QSettings(DevicesSettings.SettingsPath, DevicesSettings.SettingsFormat)

    @QtCore.Slot(result=str)
    def getDevicesConf(self):
        return self.settings.value(DevicesSettings.DevicesString, "")

    @QtCore.Slot(str)
    def storeDevicesConf(self, jsonString):
        self.settings.setValue(DevicesSettings.DevicesString, jsonString)


