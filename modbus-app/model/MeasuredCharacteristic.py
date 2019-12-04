from PyQt5.QtGui import QIcon

class MeasuredCharacteristic:

    class CharacteristicType:
        UNKNOWN = 0
        WIND_DIRECTION = 1
        WIND_STRENGTH = 2
        CO2_VALUE = 3
        ATMOSPHERE_PREASURE = 4
        TEMPERATURE = 5
        HUMIDITY = 6
        DEW_POINT = 7
        SUN_ELEVATION = 8
        SUN_AZIMUTH = 9

    class CharacteristicStrings:
        NAME = "name"
        CHARACTERISTIC_TYPE = "charType"
        VALUE = "value"
        UNIT = "unit"

    @staticmethod
    def createCharacteristic(name, charType, value, unit):
        return {
            MeasuredCharacteristic.CharacteristicStrings.NAME : name,
            MeasuredCharacteristic.CharacteristicStrings.CHARACTERISTIC_TYPE : charType,
            MeasuredCharacteristic.CharacteristicStrings.VALUE : value,
            MeasuredCharacteristic.CharacteristicStrings.UNIT : unit 
        }

    @staticmethod
    def createIcon(charType):
        iconMap =  {
            MeasuredCharacteristic.CharacteristicType.WIND_DIRECTION : QIcon(":/images/wind_direction.png") ,
            MeasuredCharacteristic.CharacteristicType.WIND_STRENGTH : QIcon(":/images/wind_speed.png") ,
            MeasuredCharacteristic.CharacteristicType.CO2_VALUE : QIcon(":/images/co2.png") ,
            MeasuredCharacteristic.CharacteristicType.ATMOSPHERE_PREASURE : QIcon(":/images/atmosphere_pressure.png") ,
            MeasuredCharacteristic.CharacteristicType.TEMPERATURE : QIcon(":/images/temperature.png") ,
            MeasuredCharacteristic.CharacteristicType.HUMIDITY : QIcon(":/images/humidity.png") ,
            MeasuredCharacteristic.CharacteristicType.DEW_POINT : QIcon(":/images/humidity.png"),
            MeasuredCharacteristic.CharacteristicType.SUN_AZIMUTH : QIcon(":/images/longitude.png") ,
            MeasuredCharacteristic.CharacteristicType.SUN_ELEVATION : QIcon(":/images/latitude.png")
        }

        return iconMap[charType]

