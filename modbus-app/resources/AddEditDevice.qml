import QtQuick 2.0
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.0

import QtQuick.Controls.Material 2.0

Popup {

    id: addEditDeviceFrame
    x: parent.left
    y: parent.right
    width: parent.width
    height: parent.height

    background: Rectangle {
         color: "#00000000"
     }

    property alias deviceText: deviceNameField.text
    property alias addressText: adressField.text
    property alias sensorType: typeCombobox.currentText
    property bool resultOk: false

    function setSensorType(sensorTypeVar)
    {
        typeCombobox.currentIndex = typeCombobox.find(sensorTypeVar)
    }


Rectangle
{
    width: 740
    height: 292
    x: (parent.width - width) /2
    y: ((parent.height - height) /2) - 30
    color: Material.color(Material.Grey, Material.Shade800)

    Text {
        id: element
        x: 8
        y: 44
        width: 213
        height: 15
        text: qsTr("Device name:")
        font.pixelSize:12
    }

    TextField {
        id: deviceNameField
        x: 265
        y: 44
        width: 424
        height: 43
        focus: Qt.inputMethod.visible;
    }

    ComboBox {
        id: typeCombobox
        x: 265
        y: 93
        width: 424
        height: 48
        model: [ "WIND SENSOR", "MULTIPLE SENSORS" ]
    }

    TextField {
        id: adressField
        x: 265
        y: 169
        width: 424
        height: 43
    }

    Text {
        id: element1
        x: 8
        y: 173
        width: 155
        height: 36
        text: qsTr("Device address(dec):")
        font.pixelSize: 12
    }

    Text {
        id: element2
        x: 8
        y: 116
        width: 138
        height: 25
        text: qsTr("Sensor type:")
        font.pixelSize: 12
    }

    Button {
        id: okButton
        x: 8
        y: 236
        width: 330
        height: 48
        text: qsTr("OK")
        onClicked: {
            resultOk = true
            addEditDeviceFrame.close()
        }
    }

    Button {
        id: cancelButton
        x: 370
        y: 236
        width: 330
        height: 48
        text: qsTr("Cancel")
        onClicked: {
            resultOk = false
            addEditDeviceFrame.close()
        }
    }
}
}
