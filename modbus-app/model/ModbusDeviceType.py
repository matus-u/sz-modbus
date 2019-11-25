import os

if os.getenv('DEVICES_ATTACHED', False) == False:
    from model.mocks import ModbusDevice
else:
    from model import ModbusDevice

class DeviceTypes:
    WIND_SENSOR = "WIND SENSOR"
    MULTIPLE_METEO = "METEO SENSOR"

    @staticmethod
    def getTypes():
        return [ DeviceTypes.WIND_SENSOR, DeviceTypes.MULTIPLE_METEO ]


    @staticmethod
    def createDevice(name, address, devType):
        if devType == DeviceTypes.WIND_SENSOR:
            return ModbusDevice.WindSensor(name, address)

        if devType == DeviceTypes.MULTIPLE_METEO:
            return ModbusDevice.MultipleMeteo(name, address)

    @staticmethod
    def getMetaCharacteristics(devType):
        return DeviceTypes.createDevice("","",devType).getMetaEmptyCharacteristics()
