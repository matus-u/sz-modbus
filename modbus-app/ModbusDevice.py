from PySide2 import QtCore

class ModbusDevice(QtCore.QObject):

    def __init__(self, serialPort, address):
        super().__init__(self)
        self.address = address 
        self._name = serialPort 
