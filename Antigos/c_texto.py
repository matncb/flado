import pytesseract
import cv2
from os import system

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('teste2.jpg')
#img = cv2.resize(img, (600, 360))

N = 5
F = 0
L = 0 
dados = (N, F, L)

def atualizar(dados):
    leitura = pytesseract.image_to_string(img) #config='-psm 10000
    leitura = leitura.upper()
    print(leitura)

    n, f, l = dados

    lista = list(leitura)
    cont = 0
    for i in lista:
        if str(i) == 'F':
            cont += 1

    f += cont
    l += n - cont

    #system('cls')
    print ("F: " + str(f))
    print ("L: " + str(l))

    return dados


dados = atualizar(dados)

cv2.imshow('Result', img)
cv2.waitKey(0)


