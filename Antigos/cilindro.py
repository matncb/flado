
from signal import raise_signal
import numpy as np
import imutils
import cv2
import time

lower = {'red': (0, 50, 70),
         'green': (36, 0, 0),
         'blue': (90, 50, 70)}

upper = {'red': (9, 255, 255),
         'green': (89, 255, 255),
         'blue': (128, 255, 255)}

colors = {'red': (0, 0, 255),
          'green': (0, 255, 0),
          'blue': (255, 0, 0)}

cilindros = {'red': [True, 0, 0], 'green': [True, 0, 0], 'blue': [True, 0, 0]}

def saida(key):
    print(str(key).title() + "---> " + "F: " + str(cilindros[key][1]) + " L: " + str(cilindros[key][2]) + " P: " + str((cilindros[key][2]/(cilindros[key][1] + cilindros[key][2]))))


while True:

    frame = cv2.imread('teste4.jpeg')

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for key, value in upper.items():
        if cilindros[key][0]:
            kernel = np.ones((9, 9), np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if radius > 0.5:
                    cilindros[key][1] += 1
                    cv2.circle(frame, (int(x), int(y)),
                            int(radius), colors[key], 2)
                    cv2.putText(frame, key + " object", (int(x-radius), int(y - radius)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[key], 2)
                else:
                    cilindros[key][2] += 1
            else:
                cilindros[key][2] += 1

            saida(key)

    cv2.imshow("Frame", frame)
    #time.sleep(2)
    cv2.waitKey(0)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()


'''
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}
'''