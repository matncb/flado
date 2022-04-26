import func
import cv2 
import numpy as np 
import imutils
from prettytable import PrettyTable 

def analise(frame, key):
    detected_circles = func.analise_circle(frame, key)

    try:
        cilindros[key] += len(detected_circles[0])
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

pasta =  './cilindros/1.6/'
n_amostra = 100

qnt_inicial = 16
cilindros = {"red": 0, "blue": 0}

qnt = qnt_inicial
for i in range(n_amostra):
    frame_path = pasta + str(i) + '.jpeg'
    frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
    #frame = imutils.resize(frame, width=600)

    analise(frame, "red")
    analise(frame, "blue")
    qnt += qnt_inicial

qnt -= qnt_inicial

output()


