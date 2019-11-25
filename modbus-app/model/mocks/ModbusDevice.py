from PyQt5 import QtCore

import random
from model.MeasuredCharacteristic import MeasuredCharacteristic

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

    def getName(self):
        return self._name
    
    def getCharacteristics(self, serialPort):
        return []

    def getMetaEmptyCharacteristics(self):
        return []

    def getSerialSpeed(self):
        return 115200

def getNumber():
    return random.randrange(10)


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = getMetaEmptyCharacteristics()
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        return chars

    def getMetaEmptyCharacteristics(self):
        return [MeasuredCharacteristic.createCharacteristic("Wind direction", MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION, "N/A", "degrees")]

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = getMetaEmptyCharacteristics()
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[2][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[3][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        chars[4][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(getNumber())
        return chars

    def getMetaEmptyCharacteristics(self):
        return [
                MeasuredCharacteristic.createCharacteristic("Temperature", MeasuredCharacteristic.CharacteristicType.TEMPERATURE, "N/A", "degrees"),
                MeasuredCharacteristic.createCharacteristic("Humidity", MeasuredCharacteristic.CharacteristicType.HUMIDITY, "N/A", "%"),
                MeasuredCharacteristic.createCharacteristic("Dew point", MeasuredCharacteristic.CharacteristicType.DEW_POINT, "N/A", "degrees"),
                MeasuredCharacteristic.createCharacteristic("Atmospheric preasure", MeasuredCharacteristic.CharacteristicType.ATMOSPHERE_PREASURE, "N/A", "hP"),
                MeasuredCharacteristic.createCharacteristic("CO2 concentration", MeasuredCharacteristic.CharacteristicType.CO2_VALUE, "N/A", "ppm")
               ]

    def getSerialSpeed(self):
        return 115200
