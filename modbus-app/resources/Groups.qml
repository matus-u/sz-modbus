import QtQuick 2.9
import QtQuick.Controls 2.2

Page {
    width: 600
    height: 400

    title: qsTr("Groups configuration")
    
    Label {
        text: qsTr("You are on Page 2.")
        anchors.centerIn: parent
    }
    
    Button {
        id: button
        x: 0
        y: 0
        width: 600
        height: 48
        text: qsTr("Add device")
    }

    ListView {
        id: listView
        x: 6
        y: 54
        width: 110
        height: 160
        delegate: Item {
            x: 5
            width: 80
            height: 40
            Row {
                id: row1
                spacing: 10
                Rectangle {
                    width: 40
                    height: 40
                    color: colorCode
                }

                Text {
                    text: name
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }

            ListElement {
                name: "Red"
                colorCode: "red"
            }

            ListElement {
                name: "Blue"
                colorCode: "blue"
            }

            ListElement {
                name: "Green"
                colorCode: "green"
            }
        }
    }
}
