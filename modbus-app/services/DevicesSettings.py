from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

import json

class DevicesSettings(QtCore.QObject):
    SettingsPath = "configs/devices.conf"
    SettingsFormat = QtCore.QSettings.NativeFormat

    DevicesString = "Devices"

    newDeviceConfigPrepared = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super().__init__()

        self.settings = QtCore.QSettings(DevicesSettings.SettingsPath, DevicesSettings.SettingsFormat)

    @QtCore.pyqtSlot(result=str)
    def getDevicesConf(self):
        return self.settings.value(DevicesSettings.DevicesString, "")

    def getDevicesConfDict(self):
        val = self.getDevicesConf()
        if val != "":
            return json.loads(self.getDevicesConf())
        return []

    @QtCore.pyqtSlot(str)
    def storeDevicesConf(self, configuration):
        self.settings.setValue(DevicesSettings.DevicesString, json.dumps(configuration))
        self.signalConfig(configuration)

    def signalConfig(self, configuration):
        self.newDeviceConfigPrepared.emit(configuration)

