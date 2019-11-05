from PySide2 import QtCore

class CharacteristicMetaData(QtCore.QObject):

    UNKNOWN = 0
    WIND_DIRECTION = 1
    WIND_STRENGTH = 2
    CO2_VALUE = 3
    ATMOSPHERE_PREASURE = 4

    def __init__(self):
        super().__init__(self)
        self._unit = ""
        self._name = ""
        self._characteristicType = self.UNKNOWN 

class CharacteristicLiveValue(QtCore.QObject):

    def __init__(self):
        super().__init__(self)
        self.characteristic_meta_data = CharacteristicMetaData()
        self.modbus_device = CharacteristicMetaData()
