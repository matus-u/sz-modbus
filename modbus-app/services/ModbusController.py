from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from services.DevicesSettings import DevicesSettings
from services.TimerService import TimerStatusObject
from model import ModbusDevice

import os

if os.getenv('DEVICES_ATTACHED', False) == False:
    from services.mocks import ModbusDialog
    from model.mocks import ModbusDevice
else:
    from services import ModbusDialog
    from model import ModbusDevice

class ModbusProxyController(QtCore.QObject):

    newConfigPrepared = QtCore.Signal(object)
    newLiveDataArrived = QtCore.Signal()

    def __init__(self, devicesSettings):
        super().__init__()
        self.deviceConfig = devicesSettings
        self.liveData = []

    @QtCore.Slot()
    def newConfigRequest(self):
        self.newConfigPrepared.emit(self.deviceConfig.getDevicesConfDict())

    @QtCore.Slot()
    def newMeasuredValues(self, newValues):
        self.liveData = newValues
        self.newLiveDataArrived.emit()

    @QtCore.Slot(result='QVariant')
    def getLiveData(self):
        return self.liveData

class ModbusController(TimerStatusObject):

    newMeasuredValues = QtCore.Signal(object)

    def __init__(self):
        super().__init__(3000)
        self.devices = []

    @QtCore.Slot()
    def newDevicesConfiguration(self, configuration):

        self.devices.clear()
        for device in configuration:
            self.devices.append(ModbusDevice.createDevice(device["name"], int(device["address"]), device["type"]))

    def onTimeout(self):
        measuredValues = {} 
        for device in self.devices:
            measuredValues.update( { device.getName() : ModbusDialog.getMeasuredValues(device) })
        self.newMeasuredValues.emit(measuredValues)

    def getProxy(self, deviceSettings):
        modbusProxy = ModbusProxyController(deviceSettings)
        modbusProxy.newConfigPrepared.connect(self.newDevicesConfiguration, QtCore.Qt.QueuedConnection)
        self.newMeasuredValues.connect(modbusProxy.newMeasuredValues, QtCore.Qt.QueuedConnection)
        return modbusProxy

