from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from generated.MainWindow import Ui_MainWindow
from ui.DevicesConfigurationWindow import DevicesConfigurationWindow

from ui import Helpers
from ui import TreeModel
from ui import SettingsWindow
from ui import WifiSettingsWindow

from services.WirelessService import WirelessService

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self, deviceSettings):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.deviceConfButton.clicked.connect(self.onDevicesConfigurationButton)
        self.ui.generalSettingsButton.clicked.connect(self.onGeneralSettings)
        self.ui.groupsConfButton.clicked.connect(self.onGroupsConfigurationButton)
        self.ui.networkSettingsButton.clicked.connect(self.onNetworkSettingsButton)
        self.deviceSettings = deviceSettings
        self.resetModel()

        self.wirelessService = WirelessService()
        #self.wirelessService.stateChanged.connect(self.wirelessServiceStateChanged)
        self.wirelessService.start()

    def openWindow(self, w):
        Helpers.openSubWindow(self, w)
        w.move(self.pos().x(), self.pos().y())

    def onGroupsConfigurationButton(self):
        pass

    def onNewLiveData(self, liveData):
        self.model.updateLiveData(liveData)

    def resetModel(self):
        self.model = TreeModel.TreeModel(self.deviceSettings.getDevicesConfDict(), [self.tr("Device"), self.tr("Char. name"), self.tr("Char. value"), self.tr("Char. unit")])
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setColumnWidth(1, 200)
        self.ui.treeView.setColumnWidth(2, 100)

    def onDevicesConfigurationButton(self):
        w = DevicesConfigurationWindow(self, self.deviceSettings.getDevicesConfDict())
        w.finished.connect(lambda retCode: self.onDevicesConfigurationFinished(retCode, w.getConfiguration()) )
        self.openWindow(w)

    def onDevicesConfigurationFinished(self, retCode, configuration):
        if retCode:
            self.deviceSettings.storeDevicesConf(configuration)
            self.resetModel()

    def onNetworkSettingsButton(self):
        self.openWindow(WifiSettingsWindow.WifiSettingsWindow(self, self.wirelessService))

    def onGeneralSettings(self):
        self.openWindow(SettingsWindow.SettingsWindow(self))

