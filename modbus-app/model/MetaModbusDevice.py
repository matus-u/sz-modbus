from model.MeasuredCharacteristic import MeasuredCharacteristic

class WindSensorMetaInfo:
    @staticmethod
    def getMetaEmptyCharacteristics():
        return [MeasuredCharacteristic.createCharacteristic("Wind direction", MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION, "N/A", "degrees")]

class MultipleMeteoSensorMetaInfo:
    @staticmethod
    def getMetaEmptyCharacteristics():
        return [
                MeasuredCharacteristic.createCharacteristic("Temperature", MeasuredCharacteristic.CharacteristicType.TEMPERATURE, "N/A", "degrees"),
                MeasuredCharacteristic.createCharacteristic("Humidity", MeasuredCharacteristic.CharacteristicType.HUMIDITY, "N/A", "%"),
                MeasuredCharacteristic.createCharacteristic("Dew point", MeasuredCharacteristic.CharacteristicType.DEW_POINT, "N/A", "degrees"),
                MeasuredCharacteristic.createCharacteristic("Atmospheric preasure", MeasuredCharacteristic.CharacteristicType.ATMOSPHERE_PREASURE, "N/A", "hP"),
                MeasuredCharacteristic.createCharacteristic("CO2 concentration", MeasuredCharacteristic.CharacteristicType.CO2_VALUE, "N/A", "ppm")
               ]

class GpsSensorMetaInfo:
    @staticmethod
    def getMetaEmptyCharacteristics():
        return [
                MeasuredCharacteristic.createCharacteristic("Sun elevation", MeasuredCharacteristic.CharacteristicType.SUN_ELEVATION, "N/A", "calc."),
                MeasuredCharacteristic.createCharacteristic("Sun azimuth", MeasuredCharacteristic.CharacteristicType.SUN_AZIMUTH, "N/A", "calc."),
               ]
