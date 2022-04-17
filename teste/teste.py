import serial

arduino = serial.Serial('COM6', 9600)

while True:
    c = input()
    if c == '1':
        arduino.write(b'1')
    elif c == '0':
        arduino.write(b'0')

    #msg = str(arduino.readline())
    #msg = msg[2:-5]
    arduino.flush()