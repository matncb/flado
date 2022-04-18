import cv2
import imutils
import serial
import time

pasta = './cilindros/0/'
camera = cv2.VideoCapture(0)

def foto(n):
    _, frame = camera.read()
    frame = imutils.resize(frame, width=600)
    cv2.imwrite(pasta + str(n) + ".jpeg", frame)


arduino = serial.Serial('COM1', 9600)

time.sleep(2)
arduino.write(b's') #comecar

n = 0
while True:
    msg = str(arduino.readline())
    msg = msg[2:-5]
    if msg == "l":
        time.sleep(2)
        foto(n)
        n += 1
        time.sleep(0.5)
        arduino.write(b's')

    arduino.flush()

