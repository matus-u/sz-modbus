from PyQt5 import QtCore

from umodbus.client.serial import rtu
from model.MeasuredCharacteristic import MeasuredCharacteristic


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


class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=1)
        response = rtu.send_message(message, serialPort)
        print (response)
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[0])
        return chars

    def getMetaEmptyCharacteristics(self):
        return [MeasuredCharacteristic.createCharacteristic("Wind direction", MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION, "N/A", "degrees")]

    def getSerialSpeed(self):
        return 9600


class MultipleMeteo(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=8)
        response = rtu.send_message(message, serialPort)
        print (response)

        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[0]/10)
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[1]/10)
        chars[2][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[2]/10)
        chars[3][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[4]/10)
        chars[4][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[5])
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
