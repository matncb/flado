import cv2 
import numpy as np 
import imutils



def pre(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    low_white = np.array([0, 42, 0])
    high_white = np.array([179, 255, 255]) #90 to 179
    white_mask = cv2.inRange(hsv, low_white, high_white)

    low_brown = np.array([5, 10, 10])
    high_brown = np.array([70, 140, 180])
    brown_mask = cv2.inRange(hsv, low_brown, high_brown)

    low_falha = np.array([90, 30, 100])
    high_falha = np.array([115, 80, 160])
    falha_mask = cv2.inRange(hsv, low_falha, high_falha)

    mask =  white_mask & cv2.bitwise_not(falha_mask) & cv2.bitwise_not(brown_mask)
    masked = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow("mask", masked)
    #cv2.waitKey(0)

    grey = mask


    #grey = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    #blur
    kernel = np.ones((5,5),np.uint8)
    grey = cv2.GaussianBlur(grey,(9,9),0)
    grey = cv2.morphologyEx(grey, cv2.MORPH_OPEN, kernel)
    grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

    #grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #grey = cv2.blur(grey, (3, 3))

    #areas escuras
    #grey = cv2.threshold(grey,100,255,cv2.THRESH_TOZERO)[1]

    #grey = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #cv2.THRESH_BINARY,11,2)[1]
    #grey = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            #cv2.THRESH_BINARY_INV,11,2)
    #grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

    img = grey
    return img

def circles(img):
    detected_circles = cv2.HoughCircles(img,
                          cv2.HOUGH_GRADIENT,
                          dp=1,
                          minDist= 5,
                          param1=70,
                          param2=18,
                          minRadius= 1,
                          maxRadius=15)

    return detected_circles


def see_circles(detected_circles, img):
    if detected_circles is not None: 
    
        detected_circles = np.uint16(np.around(detected_circles)) 
    
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            cv2.circle(img, (a, b), r, (0, 255, 0), 1) 
            cv2.circle(img, (a, b), 1, (0, 0, 255), 1) 
        cv2.imshow("Detected Circle", img) 
        cv2.waitKey(0) 

def analise_circle(frame):
    img = pre(frame)
    detected_circles = circles(img)
    show_img = frame.copy()
    #see_circles(detected_circles, show_img)
    return detected_circles


def cut_circle(frame, detected_circles, n):
    x, y, r =  [round(i) for i in detected_circles[0][n]]

    dimention = [frame.shape[0], frame.shape[1]]
    r_mask = max(dimention)
    cv2.circle(frame, (x, y), r+(round(r_mask/2)), (255, 255, 255), r_mask) 
    return frame




