import QtQuick 2.8
import QtQuick.Controls 2.2
//import Qt.labs.settings 1.0


Page {

    width: 1024
    height: 520

    title: qsTr("Page 1")

    property string datastore: ""

    Component.onCompleted: {
        var datastore = devicesSettings.getDevicesConf()
        if (datastore !== "") {
          devicesModel.clear()
          var datamodel = JSON.parse(datastore)
          for (var i = 0; i < datamodel.length; ++i) devicesModel.append(datamodel[i])
        }
    }

    Component.onDestruction: {
        var datamodel = []
        for (var i = 0; i < devicesModel.count; ++i) datamodel.push(devicesModel.get(i))
        datastore = JSON.stringify(datamodel)
        if (devicesSettings)
            devicesSettings.storeDevicesConf(datastore)
        if (modbusProxy)
            modbusProxy.newConfigRequest()
    }

    AddEditDevice {
        id: testDialog
        x: (parent.width - width) /2
        y: (parent.height - height) /2
        visible: false

        property int indexToModel: -1
        onClosed: {
            if (resultOk === true){
                if (indexToModel == -1)
                {
                    devicesModel.append({
                                            name: deviceText,
                                            address: addressText,
                                            type: sensorType,
                                            connection_type: "modbus",
                                            checked: false
                                        })
                }
                else
                {
                    devicesModel.set(indexToModel, {
                                         name: deviceText,
                                         address: addressText,
                                         type: sensorType,
                                         connection_type: "modbus",
                                         checked: devicesModel.get(indexToModel)["checked"] })
                }
            }
        }
    }

    ToolSeparator {
        id: toolSeparator
        x: 0
        y: 42
        width: parent.width
        height: 25
        orientation: Qt.Horizontal
    }

    ListView {
        id: devicesListView
        x: 0
        y: 73
        width: parent.width
        height: 447
        clip: true

        property bool checkboxesVisible: false


    delegate: Item {
        x: 5
        width: 200
        height: 60
        Row {
            Label { text: name
                font.bold: true
            }

            Rectangle
            {
                width: 50
                y: 15
                Label {
                    renderType: Text.QtRendering
                    x: 15
                    text: type
                }
            }


            Rectangle
            {
                width: 50
                y: 30
                Label {
                    renderType: Text.QtRendering
                    x: 30
                    text: connection_type
                }
            }
        }

        CheckBox{
            id: toDeleteSelectionCheckbox
            x:150
            visible: devicesListView.checkboxesVisible
            checked: model.checked
            onCheckedChanged: model.checked = checked
        }

        MouseArea {
            anchors.fill: parent
            enabled: !devicesListView.checkboxesVisible
            onClicked: {
                testDialog.deviceText = name
                testDialog.addressText = address
                testDialog.setSensorType(type)
                testDialog.indexToModel = index
                testDialog.open()
            }
        }
    }

    MouseArea {
        id: listViewArea
        anchors.fill: parent
        propagateComposedEvents: true
        onPressAndHold: {
            if (!devicesListView.checkboxesVisible){
                enabled = false
                devicesListView.checkboxesVisible = true
                devicesListView.forceLayout()
                noActionButton.visible = true
                deleteButton.visible = true
            }
        }

        onClicked: mouse.accepted = false;
    }

    model: ListModel {
        id: devicesModel
    }

    function onCheckboxActionButton() {
            noActionButton.visible = false
            deleteButton.visible = false
            devicesListView.checkboxesVisible = false
            devicesListView.forceLayout()
            listViewArea.enabled = true
    }

    Button {
        id: noActionButton
        x: 8
        y: 399
        width: 481
        height: 48
        text: qsTr("NO ACTIOn")
        visible: false
        onClicked: {
           devicesListView.onCheckboxActionButton()
        }
    }

    Button {
        id: deleteButton
        visible: false
        x: 513
        y: 399
        width: 503
        height: 48
        text: qsTr("Delete")
        onClicked: {
           var indexes = []
           for (var i=0; i < devicesModel.count; i++)
               if (devicesModel.get(i).checked)
                   indexes.push(i)

           for (var j = indexes.length; j > 0; --j)
               devicesModel.remove(indexes[j-1])
           devicesListView.onCheckboxActionButton()
        }
    }

    }


    Button {
        id: addButton
        x: 0
        y: 0
        width: parent.width
        height: 45
        text: qsTr("Add device")

        contentItem: Item {
            Row {
                layoutDirection: Qt.LeftToRight
                spacing: 5
                anchors.fill: parent
                leftPadding: 10
                Label {
                    text: addButton.text
                    font: addButton.font
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
        onClicked:  {
            testDialog.addressText = ""
            testDialog.setSensorType("WIND SENSOR")
            testDialog.deviceText = ""
            testDialog.indexToModel = -1
            testDialog.open()
        }
    }

}
