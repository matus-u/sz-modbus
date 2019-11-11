from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, QObject, QThread
from PySide2.QtQml import QQmlApplicationEngine

from generated import qml

from services.TimerService import TimerService
from services.DevicesSettings import DevicesSettings
from services.ModbusController import ModbusController

import os
import sys


def main():
    os.environ["QML2_IMPORT_PATH"]="resources/kbstyle"
    os.environ["QT_IM_MODULE"]="qtvirtualkeyboard"
    os.environ["QT_VIRTUALKEYBOARD_LAYOUT_PATH"]="resources/kbstyle/layouts"
    os.environ["QT_VIRTUALKEYBOARD_STYLE"]="modbus_app_kb"
    #os.environ["QT_LOGGING_RULES"]="qt.virtualkeyboard=true"

    app = QApplication([])

    devicesSettings = DevicesSettings()
    timerService = TimerService()
    modbusController = ModbusController()

    timerService.addTimerWorker(modbusController)
    modbusProxyController = modbusController.getProxy(devicesSettings)

    engine = QQmlApplicationEngine ()
    engine.rootContext().setContextProperty("devicesSettings", devicesSettings)
    engine.rootContext().setContextProperty("modbusProxy", modbusProxyController)
    engine.load(QUrl("qrc:/main.qml"))
    modbusProxyController.newLiveDataArrived.connect(engine.rootObjects()[0].dataArrived)

    modbusController.start()

    ret = app.exec_()

    modbusController.stop()
    timerService.quit()

    sys.exit(ret)

if __name__ == "__main__":
    main()

