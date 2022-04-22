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
                cilindros["green"] += 1
    except:
        pass
    
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

pasta =  './cilindros/666/'
n_amostra = 1

qnt_inicial = 9
cilindros = {"green": 0, "blue": 0}

qnt = qnt_inicial
for i in range(n_amostra):
    frame_path = pasta + str(i) + '.jpg'
    frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
    frame = imutils.resize(frame, width=600)

    analise(frame)
    qnt += qnt_inicial

qnt -= qnt_inicial

output()


