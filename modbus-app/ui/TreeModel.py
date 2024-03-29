from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView

from model import ModbusDeviceDict
from model import ModbusDeviceType
from model.MeasuredCharacteristic import MeasuredCharacteristic

class TreeItem(object):
    def __init__(self, data, parent=None, ico=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []
        self.ico=ico

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def children(self):
        return self.childItems

    def items(self):
        return self.itemData

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def icon(self, column):
        if self.ico:
            if column == 1:
                return self.ico
        return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0


class TreeModel(QAbstractItemModel):
    def __init__(self, configuration, headerNames, parent=None):
        super(TreeModel, self).__init__(parent)

        self.rootItem = TreeItem(headerNames)
        self.setupModelData(configuration, self.rootItem)

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            item = index.internalPointer()
            return item.data(index.column())
    
        if role == Qt.DecorationRole:
            item = index.internalPointer()
            return item.icon(index.column())

        if role == Qt.TextAlignmentRole:
            if index.column() == 2:
                return Qt.AlignRight | Qt.AlignVCenter;

        return None
        

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, configuration, rootItem):
        for dev in configuration:
            devItem = TreeItem([dev[ModbusDeviceDict.DeviceDictAccessor.NAME], "", "", ""], rootItem)
            devTypeItem = TreeItem([dev[ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE], "","", ""], devItem)
            devItem.appendChild(devTypeItem)
            for characteristic in ModbusDeviceType.DeviceTypes.getMetaCharacteristics(dev[ModbusDeviceDict.DeviceDictAccessor.DEV_TYPE]):
                charItem = TreeItem([ "", characteristic[MeasuredCharacteristic.CharacteristicStrings.NAME], characteristic[MeasuredCharacteristic.CharacteristicStrings.VALUE], characteristic[MeasuredCharacteristic.CharacteristicStrings.UNIT]], devItem, MeasuredCharacteristic.createIcon(characteristic[MeasuredCharacteristic.CharacteristicStrings.CHARACTERISTIC_TYPE]))
                devItem.appendChild(charItem)
            rootItem.appendChild(devItem)

    def updateLiveData(self, liveData):
        for dev in liveData:
            deviceName = dev[ModbusDeviceDict.DeviceDictAccessor.NAME]
            for item in self.rootItem.children():
                if deviceName == item.data(0):
                    self.updateDeviceLiveData(item, dev[ModbusDeviceDict.DeviceDictAccessor.LIVE_DATA])

    def updateDeviceLiveData(self, deviceItem, measuredValues):
        for index, valueItem in enumerate(deviceItem.children()):
            if index > 0:
                valueItem.items()[2] = measuredValues[index-1][MeasuredCharacteristic.CharacteristicStrings.VALUE]
        self.dataChanged.emit(self.createIndex(1, 2, deviceItem.child(1)), self.createIndex(deviceItem.childCount()-1, 2, deviceItem.child(deviceItem.childCount()-1)))

