# Communicating with Serial Ports

import serial
ser = serial.Serial('/dev/tty.usbmodem641', # Device  name varies
                    baudrate=9600,
                    bytesize=8,
                    parity=N,
                    sopbits=1)

ser.write(b'G1 X50 Y50'\r\n)
resp = ser.readline()

