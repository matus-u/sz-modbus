from PyQt5 import QtCore

import random
from model.MeasuredCharacteristic import MeasuredCharacteristic
from model.MetaModbusDevice import *

class ModbusDevice:
    def __init__(self, serialPort, address):
        self.address = address 
        self._name = serialPort 

    def getName(self):
        return self._name
    
def getNumber():
    return random.randrange(10)


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        return chars

    def getMetaEmptyCharacteristics(self):
        return WindSensorMetaInfo.getMetaEmptyCharacteristics()

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[2][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[3][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[4][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        return chars

    def getMetaEmptyCharacteristics(self):
        return MultipleMeteoSensorMetaInfo.getMetaEmptyCharacteristics()

    def getSerialSpeed(self):
        return 115200


class GpsSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        return chars

    def getMetaEmptyCharacteristics(self):
        return GpsSensorMetaInfo.getMetaEmptyCharacteristics()

    def getSerialSpeed(self):
        return 115200
