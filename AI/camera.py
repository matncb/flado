import cv2
import imutils
import serial
import time

pasta = './cilindros/1.1/'
camera = cv2.VideoCapture(1)

def foto(n):
    _, frame = camera.read()
    frame = imutils.resize(frame, width=600)
    cv2.imwrite(pasta + str(n) + ".jpeg", frame)


arduino = serial.Serial('COM3', 9600)

time.sleep(2)
arduino.write(b's') #comecar

n = 42 #muda com a foto
cont = 0 #sempre assim

while True:
    if cont == 10:
        time.sleep(100)
        cont = 0
    cont += 1
    msg = str(arduino.readline())
    msg = msg[2:-5]
    if msg == "l":
        time.sleep(8)
        foto(n)
        n += 1
        time.sleep(2)
        arduino.write(b's')

    arduino.flush()



