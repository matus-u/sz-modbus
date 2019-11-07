
class CharacteristicMetaData:
    UNKNOWN = 0
    WIND_DIRECTION = 1
    WIND_STRENGTH = 2
    CO2_VALUE = 3
    ATMOSPHERE_PREASURE = 4
    TEMPERATURE = 5

    def __init__(self, name, charType, value, unit):
        super().__init__(self)
        self._name = name 
        self._characteristicType = charType 
        self._value = value 
        self._unit = unit 

