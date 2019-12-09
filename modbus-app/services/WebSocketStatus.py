from PyQt5 import QtCore
from PyQt5 import QtWebSockets
from PyQt5 import QtNetwork

from services import TimerService
from services.AppSettings import AppSettings
from services.LoggingService import LoggingService

import sys
import json

class WebSocketStatus(TimerService.TimerStatusObject):

    asyncStartSignal = QtCore.pyqtSignal()
    asyncStopSignal = QtCore.pyqtSignal()

    def __init__(self, uuid):
        super().__init__(10000)
        self.uuid = uuid
        self.dataServer = AppSettings.actualDataServer()
        self.deviceName = AppSettings.actualDeviceName()
        self.websocket = QtWebSockets.QWebSocket(parent=self)
        self.connectScheduled = True

        AppSettings.getNotifier().dataServerChanged.connect(self.setDataServer)
        AppSettings.getNotifier().deviceNameChanged.connect(self.setDeviceName)

    def asyncConnect(self):
        self.asyncStartSignal.emit()

    def asyncDisconnect(self):
        self.asyncStopSignal.emit()

    def afterMove(self):
        self.asyncStartSignal.connect(self.connect, QtCore.Qt.QueuedConnection)
        self.asyncStopSignal.connect(self.forceDisconnect, QtCore.Qt.QueuedConnection)

    def setDataServer(self, val):
        self.dataServer = val
        self.asyncDisconnect()

    def setDeviceName(self, val):
        self.deviceName = val

    def onTimeout(self):
        logger = LoggingService.getLogger()
        logger.info("Update state to server with id: %s" % self.URL)

        ## APPLICATION SPECIFIC MESSAGE CREATION 
        data = {}
        textMsg = self.createPhxMessage("update-status", data)
        LoggingService.getLogger().debug("Data to websocket %s" % textMsg)
        self.websocket.sendTextMessage(textMsg)

    def forceDisconnect(self):
        if self.websocket:
            self.websocket.abort()
            self.websocket = None
        self.scheduleConnect()

    def connect(self):
        self.ref = 0
        self.connectScheduled = False
        if self.dataServer is not "":
            URL = self.dataServer + "/socket/websocket"# + self.macAddr
            self.URL = URL.replace("http://", "ws://")
            LoggingService.getLogger().info("Connecting to websocket server: %s" % URL)
            self.websocket = QtWebSockets.QWebSocket(parent=self)
            self.websocket.connected.connect(self.onConnect)
            self.websocket.disconnected.connect(self.onDisconnect)
            self.websocket.textMessageReceived.connect(self.onTextMessageReceived)
            self.websocket.open(QtCore.QUrl(self.URL))
        else:
            LoggingService.getLogger().info("Stop connecting to empty websocket!")

    def onConnect(self):
        LoggingService.getLogger().info("Connected to websocket %s" % self.URL)
        self.websocket.sendTextMessage(self.createPhxMessage( "phx_join", ""));
        self.startTimerSync()
        self.onTimeout()

    def onTextMessageReceived(self, js):
        LoggingService.getLogger().debug("Data from websocket %s" % js)
        text = json.loads(js)
        print (text)

    def onDisconnect(self):
        self.stopTimerSync()
        LoggingService.getLogger().info("Disconnected from websocket %s" % self.URL)
        self.scheduleConnect()

    def scheduleConnect(self):
        if not self.connectScheduled:
            self.connectScheduled = True
            QtCore.QTimer.singleShot(10000, self.connect)

    def createPhxMessage(self, event, payload):
        self.ref = self.ref + 1
        return json.dumps({ "topic" : "device_room:" + self.uuid,
                            "event" : event,
                            "payload" : payload,
                            "ref" : str(self.ref)
        })
