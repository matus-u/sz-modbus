from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

from services.DevicesSettings import DevicesSettings
from services.TimerService import TimerStatusObject

class ModbusProxyController(QtCore.QObject):

    newConfigPrepared = QtCore.Signal(object)

    def __init__(self, devicesSettings):
        super().__init__()
        self.deviceConfig = devicesSettings

    @QtCore.Slot()
    def newConfigRequest(self):
        print ("NEW CONFIG REQUEST")
        self.newConfigPrepared.emit(self.deviceConfig.getDevicesConfDict())
        pass


class ModbusController(TimerStatusObject):

    #devicesTransfered = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__(10000)

    @QtCore.Slot()
    def newDevicesConfiguration(self, configuration):
        print ("TODO CREATE DEVICES {}", configuration)
        pass

    def onTimeout(self):
        print ("SERIAL COMMUNICATION")

    def getProxy(self, deviceSettings):
        modbusProxy = ModbusProxyController(deviceSettings)
        modbusProxy.newConfigPrepared.connect(self.newDevicesConfiguration, QtCore.Qt.QueuedConnection)
        return modbusProxy

