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
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint);
        self.ui.deviceConfButton.clicked.connect(self.onDevicesConfigurationButton)
        self.ui.generalSettingsButton.clicked.connect(self.onLanguageSettings)
        self.ui.groupsConfButton.clicked.connect(self.onGroupsConfigurationButton)
        self.ui.networkSettingsButton.clicked.connect(self.onNetworkSettingsButton)

        self.deviceSettings = deviceSettings

    def clearStackedWidget(self):
        if (self.ui.stackedWidget.count() != 0):
            widget = self.ui.stackedWidget.currentWidget()
            self.ui.stackedWidget.removeWidget(widget)
            widget.deleteLater()

    def onGroupsConfigurationButton(self):
        self.clearStackedWidget()

    def onLanguageSettings(self):
        self.clearStackedWidget()

    def onDevicesConfigurationButton(self):
        self.clearStackedWidget()
        #self.ui.stackedWidget.addWidget(DevicesConfigurationWidget(self.deviceSettings.getDevicesConfDict()))

        w = DevicesConfigurationWindow(self, self.deviceSettings.getDevicesConfDict())
        w.finished.connect(lambda retCode: print(retCode) )
        Helpers.openSubWindow(self, w)
        w.move(self.pos().x(), self.pos().y())

    def onNetworkSettingsButton(self):
        self.clearStackedWidget()

