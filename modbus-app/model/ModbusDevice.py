from PyQt5 import QtCore

from umodbus.client.serial import rtu
from model.MeasuredCharacteristic import MeasuredCharacteristic
from model.MetaModbusDevice import *


class ModbusDevice:
    def __init__(self, serialPort, address):
        self.address = address 
        self._name = serialPort 

    def getName(self):
        return self._name
    

class WindSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=1)
        response = rtu.send_message(message, serialPort)
        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[0])
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
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=8)
        response = rtu.send_message(message, serialPort)

        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[0]/10)
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[1]/10)
        chars[2][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[2]/10)
        chars[3][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[4]/10)
        chars[4][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[5])
        return chars

    def getMetaEmptyCharacteristics(self):
        return MultipleMeteoSensorMetaInfo.getMetaEmptyCharacteristics()

    def getSerialSpeed(self):
        return 115200


class GpsSensor(ModbusDevice):
    def __init__(self, serialPort, address):
        super().__init__(serialPort, address)
    
    def getCharacteristics(self, serialPort):
        chars = self.getMetaEmptyCharacteristics()
        message = rtu.read_holding_registers(slave_id=self.address, starting_address=0, quantity=10)
        response = rtu.send_message(message, serialPort)

        chars[0][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[7])
        chars[1][MeasuredCharacteristic.CharacteristicStrings.VALUE] = str(response[8])
        return chars

    def getMetaEmptyCharacteristics(self):
        return GpsSensorMetaInfo.getMetaEmptyCharacteristics()

    def getSerialSpeed(self):
        return 9600
