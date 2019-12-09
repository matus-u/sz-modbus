class DeviceDictAccessor:
    ID = "Id"
    NAME = "Name"
    ADDRESS = "Address"
    DEV_TYPE = "DevType"

    @staticmethod
    def createDict(name, address, devType):
        return {
                DeviceDictAccessor.NAME : name,
                DeviceDictAccessor.ADDRESS : address,
                DeviceDictAccessor.DEV_TYPE : devType,
        }
