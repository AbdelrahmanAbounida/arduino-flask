import serial
import serial.tools.list_ports as ser_ports

ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,timeout=0.2)

available_ports = ser_ports.comports()

# for i in available_ports:
#     print(str(i))
# print(available_ports)

while True:
    data = ser.readline()
    if data:
        try:
            print(int(data))
        except:
            pass