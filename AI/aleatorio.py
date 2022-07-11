from cv2 import imshow
import circle, color
import cv2 
import numpy as np 
import imutils
from prettytable import PrettyTable
import random

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



pasta =  './cilindros/cartolina/V3/1.4_v3/'
n_amostra_parcial = 25
n_amostra_total = 100

qnt_inicial = 16
cilindros = {"red": 0, "blue": 0}

pos = [int(i) for i in range(n_amostra_total)]

N = 2
for i in range(N):
    random.shuffle(pos) 

qnt = qnt_inicial
for i in range(n_amostra_parcial):
    frame_path = pasta + str(pos[i]) + '.jpeg'
    frame = cv2.imread(frame_path, cv2.IMREAD_COLOR)
    frame = imutils.resize(frame, width=600)

    analise(frame)
    qnt += qnt_inicial

qnt -= qnt_inicial

def pegar():
    return p(0)
