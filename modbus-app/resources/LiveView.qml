import QtQuick 2.9
import QtQuick.Controls 2.2

import QtQuick.Controls.Material 2.0

Page {
    width: 1024
    height: 520

    title: qsTr("Live view")

    function refreshData()
    {
        if (modbusProxy)
            var l = modbusProxy.getLiveData()
        liveDataModel.clear()
        for (var data in l) {
            var subModel = []
            liveDataModel.append({ name : data,
                                     values : l[data]
                                 })
        }
    }

    Component.onCompleted: {
        refreshData()
    }
    ScrollView
    {
        width: parent.width - 10
        height: parent.height - 10
        x: 5
        y: 5


        GridView {
            id: liveDataListView
            anchors.fill: parent

            cellHeight: 150

            cellWidth: 250

            delegate: deviceDelegate

            model: ListModel {
                id: liveDataModel
            }
        }

        Component {
            id: deviceDelegate

            Rectangle
            {
                width: liveDataListView.cellWidth - 10
                height: liveDataListView.cellHeight - 10
                x: 5
                y: 5
                color: Material.color(Material.Grey, Material.Shade600)
                border.color: Material.color(Material.Grey, Material.Shade700)
                //border.width: 2
                radius: 0.01

                Column {
                    width: parent.width - 20
                    height: parent.height - 20
                    x: 10
                    y: 10
                    spacing: 5
                    Label {
                        id: deviceName
                        text: "Name: " + name
                    }
                    Rectangle
                    {
                        width: parent.width
                        color: Material.color(Material.Grey, Material.Shade500)
                        height: 100

                        Flickable {
                            anchors.fill: parent
                            clip: true
                            contentWidth: col.implicitWidth
                            contentHeight: col.height
                            Column {
                                id: col
                                spacing: 5

                                Repeater {
                                    model: values
                                    delegate: characteristicDelegate
                                }
                            }
                            ScrollBar.vertical: ScrollBar { policy: ScrollBar.AlwaysOn }
                        }

                    }
                }
            }
        }

        Component {
            id: characteristicDelegate
            Column
            {
                Row {

                    Label {
                        text: name + ":"
                    }
                }
                Row {

                    Label {
                        text: value + " " + unit
                    }
                }

            }
        }
    }
}
