import cv2
import serial
import time
pasta = './cilindros/1.6_v2/'
camera = cv2.VideoCapture(1)

def foto(n):
    _, frame = camera.read()
    cv2.imwrite(pasta + str(n) + ".jpeg", frame)


arduino = serial.Serial('COM8', 9600)

n = 97 #muda com a foto
cont = 0 #sempre assim

time.sleep(2)
arduino.write(b's') #comecar

msg = None

while True:
    if cont == 10:
        print('contador : ' + str(cont))
        print('Esperando 30s')
        time.sleep(25)
        print('5 seg')
        time.sleep(5)
        cont = 0
    msg = str(arduino.readline())
    msg = msg[2:-5]
    print('mensagem recebida: ' + msg)
    if msg == "l":
        print('contador: ' + str(cont))
        msg = None
        time.sleep(4)
        foto(n)
        n += 1
        cont += 1

        time.sleep(0.5)
        arduino.write(b's')
    else:
        arduino.write(b's')
        
 
    arduino.flush()



