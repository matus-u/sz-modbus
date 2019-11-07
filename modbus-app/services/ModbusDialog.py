import fcntl
import struct
from serial import Serial, PARITY_NONE

from umodbus.client.serial import rtu

def getSerialPort(baud):
    try:
        port = Serial(port='/dev/ttyUSB0', baudrate=baud, parity=PARITY_NONE,
                      stopbits=1, bytesize=8, timeout=1)
        #serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
        #fcntl.ioctl(fh, 0x542F, serial_rs485)
        return port
    except:
        return None


def getMeasuredValues(device):
    measuredValues = []
    port = getSerialPort(device.getSerialSpeed())
    if port:
        try:
            measuredValues.extend(device.getCharacteristics(port))
        finally:
            port.close()
    return measuredValues



