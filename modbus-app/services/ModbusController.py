from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from services.DevicesSettings import DevicesSettings
from services.TimerService import TimerStatusObject

import os

if os.getenv('DEVICES_ATTACHED', False) == False:
    from services.mocks import ModbusDialog
else:
    from services import ModbusDialog

from model import ModbusDeviceType

class ModbusProxyController(QtCore.QObject):

    newConfigPrepared = QtCore.pyqtSignal('PyQt_PyObject')
    newLiveDataArrived = QtCore.pyqtSignal()

    def __init__(self, devicesSettings):
        super().__init__()
        self.deviceConfig = devicesSettings
        self.liveData = []

    @QtCore.pyqtSlot()
    def newConfigRequest(self):
        self.newConfigPrepared.emit(self.deviceConfig.getDevicesConfDict())

    @QtCore.pyqtSlot(object)
    def newMeasuredValues(self, newValues):
        self.liveData = newValues
        self.newLiveDataArrived.emit()

    @QtCore.pyqtSlot(result='QVariant')
    def getLiveData(self):
        return self.liveData

class ModbusController(TimerStatusObject):

    newMeasuredValues = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super().__init__(3000)
        self.devices = []

    @QtCore.pyqtSlot(dict)
    def newDevicesConfiguration(self, configuration):
        self.devices.clear()
        for device in configuration:
            self.devices.append(ModbusDeviceType.DeviceTypes.createDevice(device["name"], int(device["address"]), device["type"]))

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

