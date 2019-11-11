from PySide2 import QtCore

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

    def getSerialSpeed(self):
        return 115200

def getNumber():
    return random.randrange(10)


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        return [MeasuredCharacteristic.createCharacteristic("Wind direction", MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION, getNumber(), "degrees")]

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        return [
                MeasuredCharacteristic.createCharacteristic("Temperature", MeasuredCharacteristic.CharacteristicType.TEMPERATURE, getNumber(), "degrees"),
                MeasuredCharacteristic.createCharacteristic("Humidity", MeasuredCharacteristic.CharacteristicType.HUMIDITY, getNumber(), "%"),
                MeasuredCharacteristic.createCharacteristic("Atmospheric preasure", MeasuredCharacteristic.CharacteristicType.ATMOSPHERE_PREASURE, getNumber(), "hP"),
                MeasuredCharacteristic.createCharacteristic("CO2 concentration", MeasuredCharacteristic.CharacteristicType.CO2_VALUE, getNumber(), "ppm")
               ]

    def getSerialSpeed(self):
        return 115200
