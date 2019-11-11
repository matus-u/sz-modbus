import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Window 2.0
import QtQuick.VirtualKeyboard 2.1

ApplicationWindow {
    id: window
    visible: true
    width: 1024
    height: 600
    title: qsTr("Stack")
    flags: Qt.Window | Qt.FramelessWindowHint

    function dataArrived()
    {
        liveView.refreshData()
    }

    header: ToolBar {
        position: ToolBar.Header
        contentHeight: toolButton.implicitHeight

        ToolButton {
            id: toolButton
            text: stackView.depth > 1 ? "\u25C0" : "\u2630"
            font.pixelSize: Qt.application.font.pixelSize * 1.6
            onClicked: {
                if (stackView.depth > 1) {
                    stackView.pop()
                } else {
                    drawer.open()
                }
            }
        }

        Label {
            text: stackView.currentItem.title
            anchors.centerIn: parent
        }
    }

    Drawer {
        id: drawer
        width: window.width * 0.66
        height: window.height

        objectName: "drawer"

        Column {
            anchors.fill: parent

            ItemDelegate {
                text: qsTr("Devices")
                width: parent.width
                onClicked: {
                    stackView.push("Devices.qml")
                    drawer.close()
                }
            }
            ItemDelegate {
                text: qsTr("Groups")
                width: parent.width
                onClicked: {
                    stackView.push("Groups.qml")
                    drawer.close()
                }
            }
        }
    }

    LiveView
    {
        id: liveView
    }

    StackView {
        id: stackView
        initialItem: liveView
        anchors.fill: parent

        TextField {
            id: textField
            x: 328
            y: 128
            text: qsTr("Text Field")
        }
    }

    InputPanel {
        id: inputPanel
        parent: ApplicationWindow.overlay
        y: active ? parent.height - height : parent.height
        z:1
        visible: Qt.inputMethod.visible;
        anchors.left: parent.left
        anchors.right: parent.right

    }

    Component.onCompleted: {
        if (modbusProxy)
            modbusProxy.newConfigRequest()
    }


}
