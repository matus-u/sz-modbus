def getMeasuredValues(device):
    speed = (device.getSerialSpeed())
    return device.getCharacteristics(speed)
