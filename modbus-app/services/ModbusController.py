from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from services.DevicesSettings import DevicesSettings
from services.TimerService import TimerStatusObject
from model import ModbusDevice

import os

if os.getenv('RUN_FROM_DOCKER', False) == False:
    from services import ModbusDialog
    from model import ModbusDevice
else:
    from services.mocks import ModbusDialog
    from model.mocks import ModbusDevice

class ModbusProxyController(QtCore.QObject):

    newConfigPrepared = QtCore.Signal(object)

    def __init__(self, devicesSettings):
        super().__init__()
        self.deviceConfig = devicesSettings

    @QtCore.Slot()
    def newConfigRequest(self):
        self.newConfigPrepared.emit(self.deviceConfig.getDevicesConfDict())
        pass


class ModbusController(TimerStatusObject):

    def __init__(self):
        super().__init__(1000)
        self.devices = []

    @QtCore.Slot()
    def newDevicesConfiguration(self, configuration):
        print ("TODO CREATE DEVICES {}", configuration)

        self.devices.clear()
        for device in configuration:
            self.devices.append(ModbusDevice.createDevice(device["name"], device["address"], device["type"]))

    def onTimeout(self):
        measuredValues = [] 
        for device in self.devices:
            measuredValues.extend(ModbusDialog.getMeasuredValues(device))

    def getProxy(self, deviceSettings):
        modbusProxy = ModbusProxyController(deviceSettings)
        modbusProxy.newConfigPrepared.connect(self.newDevicesConfiguration, QtCore.Qt.QueuedConnection)
        return modbusProxy

