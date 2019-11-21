class DeviceTypes:
    WIND_SENSOR = "WIND SENSOR"
    MULTIPLE_METEO = "METEO SENSOR"

    @staticmethod
    def getTypes():
        return [ DeviceTypes.WIND_SENSOR, DeviceTypes.MULTIPLE_METEO ]

