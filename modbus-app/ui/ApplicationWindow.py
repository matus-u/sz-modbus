from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.MainWindow import Ui_MainWindow
from ui.DevicesConfigurationWindow import DevicesConfigurationWindow
from ui import Helpers

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self, deviceSettings):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.deviceConfButton.clicked.connect(self.onDevicesConfigurationButton)
        self.ui.generalSettingsButton.clicked.connect(self.onLanguageSettings)
        self.ui.groupsConfButton.clicked.connect(self.onGroupsConfigurationButton)
        self.ui.networkSettingsButton.clicked.connect(self.onNetworkSettingsButton)

        self.deviceSettings = deviceSettings

    def onGroupsConfigurationButton(self):
        pass


    def onDevicesConfigurationButton(self):
        w = DevicesConfigurationWindow(self, self.deviceSettings.getDevicesConfDict())
        w.finished.connect(lambda retCode: self.onDevicesConfigurationFinished(retCode, w.getConfiguration()) )
        Helpers.openSubWindow(self, w)
        w.move(self.pos().x(), self.pos().y())

    def onDevicesConfigurationFinished(self, retCode, configuration):
        if retCode:
            self.deviceSettings.storeDevicesConf(configuration)

    def onNetworkSettingsButton(self):
        pass

    def onLanguageSettings(self):
        pass

