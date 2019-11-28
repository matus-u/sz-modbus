from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class AppSettingsNotifier(QtCore.QObject):

    dataServerChanged = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()


class AppSettings:
    SettingsPath = "configs/mod-app.conf"
    SettingsFormat = QtCore.QSettings.NativeFormat
    TimeZoneList = ["UTC","Europe/Budapest","Europe/Bratislava","Europe/London"]
    LanguageList = ["english","hungarian","slovak"]
    LanguageString = "language"
    TimeZoneString = "timezone"
    Translator = QtCore.QTranslator()

    WirelessSettingsPath = "configs/wireless.conf"
    WirelessEnabledString = "Enabled"
    SSIDString = "SSID"
    WirelessPassString = "WirelessPass"

    AppVersion = "1.0"
    DeviceNameString = "DeviceName"
    ServicePhoneString = "ServicePhone"
    DescString = "Description"
    DataServerString = "DataServer"

    Notifier = AppSettingsNotifier()

    @staticmethod
    def checkSettingsMap(settings, path):
        if settings is not None:
            return settings
        else:
            return QtCore.QSettings(path, AppSettings.SettingsFormat)

    @staticmethod
    def checkSettingsParam(settings):
        return AppSettings.checkSettingsMap(settings, AppSettings.SettingsPath)

    @staticmethod
    def checkWifiSettingsParam(settings):
        return AppSettings.checkSettingsMap(settings, AppSettings.WirelessSettingsPath)

    @staticmethod
    def actualAppVersion():
        return AppSettings.AppVersion

    @staticmethod
    def actualLanguage(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.LanguageString, AppSettings.LanguageList[0])

    @staticmethod
    def getCurrentLanguageIndex():
        return AppSettings.LanguageList.index(AppSettings.actualLanguage())

    @classmethod
    def restoreLanguage(cls):
        cls._loadLanguage(AppSettings.actualLanguage())

    @classmethod
    def restoreTimeZone(cls):
        QtCore.QProcess.execute("scripts/set-time-zone.sh", [AppSettings.actualTimeZone()])

    @staticmethod
    def actualTimeZone(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.TimeZoneString, AppSettings.TimeZoneList[0])

    @staticmethod
    def getCurrentTimeZoneIndex():
        return AppSettings.TimeZoneList.index(AppSettings.actualTimeZone())

    @staticmethod
    def actualDataServer(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.DataServerString, "")

    @classmethod
    def loadLanguageByIndex(cls, index):
        cls._loadLanguage(AppSettings.LanguageList[index])

    @classmethod
    def _loadLanguage(cls, language):
        app = QtWidgets.QApplication.instance()
        app.removeTranslator(cls.Translator)
        cls.Translator = QtCore.QTranslator()
        cls.Translator.load(language + ".qm", "./translation")
        app.installTranslator(cls.Translator)
        QtCore.QCoreApplication.processEvents()

    @classmethod
    def storeSettings(cls, languageIndex, timeZoneIndex, dataServer):
        settings = QtCore.QSettings(AppSettings.SettingsPath, AppSettings.SettingsFormat)
        settings.setValue(AppSettings.LanguageString, AppSettings.LanguageList[languageIndex])
        settings.setValue(AppSettings.TimeZoneString, AppSettings.TimeZoneList[timeZoneIndex])
        if dataServer != AppSettings.actualDataServer(settings):
            settings.setValue(AppSettings.DataServerString, dataServer)
            cls.getNotifier().dataServerChanged.emit(dataServer)
        settings.sync()
        QtCore.QProcess.execute("scripts/set-time-zone.sh", [AppSettings.TimeZoneList[timeZoneIndex]])


    @classmethod
    def storeWirelessSettings(cls, enabled, SSID, password):
        settings = QtCore.QSettings(AppSettings.WirelessSettingsPath, AppSettings.SettingsFormat)
        settings.setValue(AppSettings.WirelessEnabledString, enabled)
        settings.setValue(AppSettings.SSIDString, SSID)
        settings.setValue(AppSettings.WirelessPassString, password)
        settings.sync()

    @staticmethod
    def actualWirelessEnabled(appSettings = None):
        return AppSettings.checkWifiSettingsParam(appSettings).value(AppSettings.WirelessEnabledString, False, bool)

    @staticmethod
    def actualWirelessSSID(appSettings = None):
        return AppSettings.checkWifiSettingsParam(appSettings).value(AppSettings.SSIDString, "")

    @staticmethod
    def actualWirelessPassword(appSettings = None):
        return AppSettings.checkWifiSettingsParam(appSettings).value(AppSettings.WirelessPassString, "")

    @staticmethod
    def actualDeviceName(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.DeviceNameString, "")

    @staticmethod
    def actualDescription(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.DescString, "")

    @staticmethod
    def actualServicePhone(appSettings = None):
        return AppSettings.checkSettingsParam(appSettings).value(AppSettings.ServicePhoneString, "")

    @classmethod
    def storeServerSettings(cls, name, desc, servicePhone):
        settings = QtCore.QSettings(AppSettings.SettingsPath, AppSettings.SettingsFormat)
        if name is not None:
            if name != AppSettings.actualDeviceName(settings):
                settings.setValue(AppSettings.DeviceNameString, name)
                cls.getNotifier().deviceNameChanged.emit(name)
        if desc is not None:
            settings.setValue(AppSettings.DescString, desc)
        if servicePhone is not None:
            if servicePhone != AppSettings.actualServicePhone(settings):
                settings.setValue(AppSettings.ServicePhoneString, servicePhone)
                cls.getNotifier().servicePhoneChanged.emit(servicePhone)
        settings.sync()

    @classmethod
    def getNotifier(cls):
        return cls.Notifier

