from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from services.DevicesSettings import DevicesSettings
from services.TimerService import TimerStatusObject

from model.ModbusDeviceDict import DeviceDictAccessor

import os

if os.getenv('DEVICES_ATTACHED', False) == False:
    from services.mocks import ModbusDialog
else:
    from services import ModbusDialog

from model import ModbusDeviceType

class ModbusController(TimerStatusObject):

    newMeasuredValues = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self):
        super().__init__(3000)
        self.devices = []
        self.configuration = {}

    @QtCore.pyqtSlot(dict)
    def newDevicesConfiguration(self, configuration):
        self.devices.clear()
        self.configuration = configuration
        for device in configuration:
            self.devices.append(ModbusDeviceType.DeviceTypes.createDevice(device[DeviceDictAccessor.ID], int(device[DeviceDictAccessor.ADDRESS]), device[DeviceDictAccessor.DEV_TYPE]))

    def onTimeout(self):
        config = self.configuration
        tmp = {}
        for device in self.devices:
            tmp.update( { device.getName() : ModbusDialog.getMeasuredValues(device) })

        for device in config:
            device.update({DeviceDictAccessor.LIVE_DATA : tmp[device[DeviceDictAccessor.ID]]})

        self.newMeasuredValues.emit(config)

