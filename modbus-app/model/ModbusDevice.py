from PySide2 import QtCore

from umodbus.client.serial import rtu
from model.MeasuredCharacteristic import MeasuredCharacteristic

def createDevice(name, address, devType):
    if devType == "WIND SENSOR":
        return WindSensor(name, address)

    if devType == "MULTIPLE SENSORS":
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


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=1)
        response = rtu.send_message(message, serialPort)
        print (response)
        return [MeasuredCharacteristic.createCharacteristic("Wind direction", MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION, response[0], "degrees")
                ]

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=8)
        response = rtu.send_message(message, serialPort)
        print (response)
        return [
                MeasuredCharacteristic.createCharacteristic("Temperature", MeasuredCharacteristic.CharacteristicType.TEMPERATURE, response[0]/10, "degrees"),
                MeasuredCharacteristic.createCharacteristic("Humidity", MeasuredCharacteristic.CharacteristicType.HUMIDITY, response[1]/10, "%"),
                MeasuredCharacteristic.createCharacteristic("Atmospheric preasure", MeasuredCharacteristic.CharacteristicType.ATMOSPHERE_PREASURE, response[4]/10, "hP"),
                MeasuredCharacteristic.createCharacteristic("CO2 concentration", MeasuredCharacteristic.CharacteristicType.CO2_VALUE, response[5], "ppm")
               ]


    def getSerialSpeed(self):
        return 115200
