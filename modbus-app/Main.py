from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine

from generated import qml

from services.DevicesSettings import DevicesSettings

import os

def main():
    os.environ["QML2_IMPORT_PATH"]="resources/kbstyle"
    os.environ["QT_IM_MODULE"]="qtvirtualkeyboard"
    os.environ["QT_VIRTUALKEYBOARD_LAYOUT_PATH"]="resources/kbstyle/layouts"
    os.environ["QT_VIRTUALKEYBOARD_STYLE"]="modbus_app_kb"
    #os.environ["QT_LOGGING_RULES"]="qt.virtualkeyboard=true"

    app = QApplication([])
    devicesSettings = DevicesSettings()
    engine = QQmlApplicationEngine ()
    engine.rootContext().setContextProperty("devicesSettings", devicesSettings)
    engine.load(QUrl("qrc:/main.qml"))

    return app.exec_()

if __name__ == "__main__":
    main()

