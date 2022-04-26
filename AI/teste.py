import cv2 
import numpy as np 

frame = cv2.imread('parede.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

print(hsv)