from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QThread
from PyQt5 import QtCore
from PyQt5 import QtWidgets


from services.AppSettings import AppSettings
from services.LoggingService import LoggingService
from services.TimerService import TimerService
from services.DevicesSettings import DevicesSettings
from services.ModbusController import ModbusController
from services.GuidTracker import GuidTracker
from services.WebSocketStatus import WebSocketStatus

from ui import ApplicationWindow

import os
import sys

from generated import themes

def setStyle(app):
    #QApplication.setStyle(QtWidgets.QStyleFactory.create("motif"))
    styleFile = QtCore.QFile(":/dark-orange.qss")
    styleFile.open(QtCore.QIODevice.ReadOnly)
    data = styleFile.readAll()
    app.setStyleSheet(str(data, encoding="utf-8"))

def main():
    os.environ["QML2_IMPORT_PATH"]="resources/kbstyle"
    os.environ["QT_IM_MODULE"]="qtvirtualkeyboard"
    os.environ["QT_VIRTUALKEYBOARD_LAYOUT_PATH"]="resources/kbstyle/layouts"
    os.environ["QT_VIRTUALKEYBOARD_STYLE"]="modbus_app_kb"
    #os.environ["QT_LOGGING_RULES"]="qt.virtualkeyboard=true"

    LoggingService.init()
    app = QApplication(sys.argv)
    setStyle(app)

    AppSettings.restoreLanguage()
    AppSettings.restoreTimeZone()

    #Settings
    guidTracker = GuidTracker()
    devicesSettings = DevicesSettings()

    #Remote update
    updateStatusTimerService = TimerService()
    webUpdateStatus = WebSocketStatus(guidTracker.getGuid())
    updateStatusTimerService.addTimerWorker(webUpdateStatus)

    #Local data
    timerService = TimerService()
    modbusController = ModbusController()
    timerService.addTimerWorker(modbusController)

    modbusController.start()

    #MainWindow
    application = ApplicationWindow.ApplicationWindow(devicesSettings)

    modbusController.newMeasuredValues.connect(application.onNewLiveData, QtCore.Qt.QueuedConnection)
    devicesSettings.newDeviceConfigPrepared.connect(modbusController.newDevicesConfiguration, QtCore.Qt.QueuedConnection)
    devicesSettings.signalConfig(devicesSettings.getDevicesConfDict())

    modbusController.newMeasuredValues.connect(webUpdateStatus.onNewLiveData, QtCore.Qt.QueuedConnection)

    #Start the app
    application.show()
    webUpdateStatus.asyncConnect()

    ret = app.exec_()
    modbusController.stop()
    webUpdateStatus.asyncDisconnect()
    updateStatusTimerService.quit()
    timerService.quit()
    sys.exit(ret)

if __name__ == "__main__":
    main()

