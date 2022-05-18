from cv2 import imshow
import circle, color
import cv2 
import numpy as np 
import imutils
from prettytable import PrettyTable 

def analise(frame):
    detected_circles = circle.analise_circle(frame)

    try:
        for n in range(len(detected_circles[0])):
            frame_cor = frame.copy()
            cor = color.analise_color(circle.cut_circle(frame_cor, detected_circles, n))
            if cor == "blue":
                cilindros["blue"] += 1
            else:
                cilindros["red"] += 1
    except:
        pass
    
def p(cor):
    if cor == 'red':
        return cilindros["red"]/qnt
    if cor == 'blue':
        return cilindros['blue']/qnt
    else:
        return (qnt - cilindros['red'] - cilindros['blue'])/qnt

def output():
    myTable = PrettyTable(["", "Face 1 (vermelho)", "Face 2 (azul)", "  Lado  "]) 
    myTable.add_row(["Quantidade", cilindros['red'], cilindros['blue'], (qnt - cilindros['red'] - cilindros['blue'])])
    myTable.add_row(["Probabilidade", str(round((p('red')*100), 2)) + '%', str(round(p('blue')*100, 2)) + '%', str(round(p(0)*100, 2)) + '%']) 
 
    print(myTable)

pasta =  './cilindros/V3_2.0/2.5_v3_2.0/'
n_amostra = 100

qnt_inicial = 16
cilindros = {"red": 0, "blue": 0}

qnt = qnt_inicial
for i in range(n_amostra):
    frame_path = pasta + str(i) + '.jpeg'
    frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
    frame = imutils.resize(frame, width=600)

    analise(frame)
    qnt += qnt_inicial

qnt -= qnt_inicial

output()


