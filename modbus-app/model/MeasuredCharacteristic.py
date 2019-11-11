
class MeasuredCharacteristic:

    class CharacteristicType:
        UNKNOWN = 0
        WIND_DIRECTION = 1
        WIND_STRENGTH = 2
        CO2_VALUE = 3
        ATMOSPHERE_PREASURE = 4
        TEMPERATURE = 5
        HUMIDITY = 5

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

