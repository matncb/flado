import cv2
import serial
import time
pasta = './cilindros/camurca/V2_2.0/0.7_v2_2.0/'
camera = cv2.VideoCapture(0)

def foto(n):
    _, frame = camera.read()
    cv2.imwrite(pasta + str(n) + ".jpeg", frame)


arduino = serial.Serial('COM3', 9600)

n = 75 #muda com a foto
cont = 0 #sempre assim

#arduino.write(b's') #comecar

msg = None

while True:
    msg = arduino.readline()
    if msg:
        print('contador: ' + str(cont))
        msg = None
        time.sleep(3.5)
        foto(n)
        n += 1
        cont += 1 
        arduino.flush()



