from cv2 import imshow
import circle, color
import cv2 
import numpy as np 
import imutils
from prettytable import PrettyTable 

#camera = cv2.VideoCapture('http://192.168.0.101:4747/mjpegfeed?600x600')

def foto():
    #_, frame = camera.read()
    frame = cv2.imread('../teste/teste1.jpeg', cv2.IMREAD_COLOR)
    frame = imutils.resize(frame, width=600)
    return frame

def analise(frame):
    detected_circles = circle.analise_circle(frame)

    for n in range(len(detected_circles[0])):
        frame_cor = frame.copy()
        cor = color.analise_color(circle.cut_circle(frame_cor, detected_circles, n))
        if cor == "green":
            cilindros["green"] += 1
        else:
            cilindros["blue"] += 1

def p(cor):
    if cor == 'green':
        return cilindros["green"]/qnt
    if cor == 'blue':
        return cilindros['blue']/qnt
    else:
        return (qnt - cilindros['green'] - cilindros['blue'])/qnt

def output():
    myTable = PrettyTable(["", "Face 1 (verde)", "Face 2 (azul)", "  Lado  "]) 
    myTable.add_row(["Quantidade", cilindros['green'], cilindros['blue'], (qnt - cilindros['green'] - cilindros['blue'])])
    myTable.add_row(["Probabilidade", str(round((p('green')*100), 2)) + '%', str(round(p('blue')*100, 2)) + '%', str(round(p(0)*100, 2)) + '%']) 
 
    print(myTable)

#analise(foto())
#output()

pasta =  './cilindros/0/'
n_amostra = 4

qnt_inicial = 3
cilindros = {"green": 0, "blue": 0}

qnt = qnt_inicial
for i in range(n_amostra):
    frame_path = pasta + str(i) + '.jpeg'
    frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
    frame = imutils.resize(frame, width=600)

    analise(frame)
    qnt += qnt_inicial

qnt -= qnt_inicial

output()


