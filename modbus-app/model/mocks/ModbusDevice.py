from PySide2 import QtCore

def createDevice(name, address, devType):
    if devType == "WIND SENSOR":
        print ("CREATE WIND")
        return WindSensor(name, address)

    if devType == "MULTIPLE SENSORS":
        print ("CREATE MULTIPLE")
        return MultipleMeteo(name, address)

class ModbusDevice:
    def __init__(self, serialPort, address):
        self.address = address 
        self._name = serialPort 
    
    def getCharacteristics(self, serialPort):
        return []

    def getSerialSpeed(self):
        return 115200


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        print ("WIND SENSOR")
        return []

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        print ("WIND METEOSENSOR")
        return []

    def getSerialSpeed(self):
        return 115200
