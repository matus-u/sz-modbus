from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class GuidTracker(QtCore.QObject):
    SettingsPath = "configs/guid.conf"
    SettingsFormat = QtCore.QSettings.NativeFormat

    Guid = "Guid"

    def __init__(self):
        super().__init__()

        settings = QtCore.QSettings(GuidTracker.SettingsPath, GuidTracker.SettingsFormat)
        self.guid = settings.value(GuidTracker.Guid, "")
        
        if self.guid == "":
            self.guid = QtCore.QUuid.createUuid().toString()
            settings.setValue(GuidTracker.Guid, self.guid)
            settings.sync()

    def getGuid(self):
        return self.guid

