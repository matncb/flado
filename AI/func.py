import cv2 
import numpy as np 
import imutils


def pre(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    white_mask = cv2.inRange(hsv, low, high)
    result = cv2.bitwise_and(frame, frame, mask=white_mask)
    

    grey = white_mask

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
                          param2=20,
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
        cv2.imshow(key, img) 
        cv2.waitKey(0) 

def analise_circle(frame):
    img = pre(frame)
    detected_circles = circles(img)
    show_img = frame.copy()
    see_circles(detected_circles, show_img)
    return detected_circles
