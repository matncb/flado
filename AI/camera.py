import cv2
import serial
import time
pasta = './cilindros/V3_2.0/2.5_v3_2.0/'
camera = cv2.VideoCapture(1)

def foto(n):
    _, frame = camera.read()
    cv2.imwrite(pasta + str(n) + ".jpeg", frame)


arduino = serial.Serial('COM9', 9600)

n = 10 #muda com a foto
cont = 0 #sempre assim

#arduino.write(b's') #comecar

msg = None

'''
while True:
    if cont == 10:
        print('contador : ' + str(cont))
        print('Esperando 30s')
        time.sleep(25)
        print('5 seg')
        time.sleep(5)
        cont = 0
    msg = arduino.readline()
    if msg:
        print('contador: ' + str(cont))
        msg = None
        time.sleep(4)
        foto(n)
        n += 1
        cont += 1

        #time.sleep(0.5)
        #arduino.write(b's')   
        arduino.flush()
    else:
        #arduino.write(b's')
        pass
'''
while True:
    msg = arduino.readline()
    if msg:
        print('contador: ' + str(cont))
        msg = None
        time.sleep(4)
        foto(n)
        n += 1
        cont += 1 
        arduino.flush()
'''

def read_line_c(ser):
    buf = bytearray()
    i = buf.find(b"\r")
    if i >= 0:
        r = buf[:i + 1]
        buf[i + 1:]
        return r
    while True:
        i = max(1, min(2048, ser.in_waiting))
        data = ser.read(i)
        i = data.find(b"\r")
        print("loop")
        if i >= 0:
            r = buf + data[:i + 1]
            buf[0:] = data[i + 1:]
            return r
        else:
            buf.extend(data)

while True:
    msg = arduino.readline()
    print(msg)
    time.sleep(1)
    arduino.write(b's')
    arduino.flush()
'''

