#!/usr/bin/env python
# scripts/example/simple_rtu_client.py
import fcntl
import struct
from serial import Serial, PARITY_NONE

from umodbus.client.serial import rtu


def get_serial_port(baud):
    """ Return serial.Serial instance, ready to use for RS485."""
    port = Serial(port='/dev/ttyUSB0', baudrate=baud, parity=PARITY_NONE,
                  stopbits=1, bytesize=8, timeout=1)

#    fh = port.fileno()
    print (port)

    # A struct with configuration for serial port.
    #serial_rs485 = struct.pack('hhhhhhhh', 1, 0, 0, 0, 0, 0, 0, 0)
    #fcntl.ioctl(fh, 0x542F, serial_rs485)

    return port


serial_port_9600 = get_serial_port(9600)
message = rtu.read_holding_registers(slave_id=1, starting_address=0, quantity=1)
response = rtu.send_message(message, serial_port_9600)
print (response)

serial_port_9600.close()

serial_port_9600 = get_serial_port(9600)
message = rtu.read_holding_registers(slave_id=4, starting_address=0, quantity=10)
response = rtu.send_message(message, serial_port_9600)
print (response)

serial_port_9600.close()
quit()


serial_port_9600 = get_serial_port(9600)
#serial_port_115200 = get_serial_port(115200)

## Returns a message or Application Data Unit (ADU) specific for doing
## Modbus RTU.
#message = rtu.read_holding_registers(slave_id=64, starting_address=0, quantity=10)
##
### Response depends on Modbus function code. This particular returns the
### amount of coils written, in this case it is.
#response = rtu.send_message(message, serial_port_115200)
#print (response)
#message = rtu.write_multiple_registers(slave_id=96, starting_address=0, values=[2, 0x476f, 0x6f64, 0x2064])
# Response depends on Modbus function code. This particular returns the
# amount of coils written, in this case it is.
for i in range (0,256):
    try:
        message = rtu.read_holding_registers(slave_id=i, starting_address=0, quantity=10)
        response = rtu.send_message(message, serial_port_9600)
        print (i)
        print (response)
    except:
        pass


serial_port_9600.close()
#serial_port_115200.close()

