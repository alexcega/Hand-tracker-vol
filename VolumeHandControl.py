import cv2 as cv
import time
import numpy as np
import HandTrackingModule
############################
wCam, hCam = 640, 480
############################

cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, f'FPS: {int(fps)}', (40,50), cv.FONT_HERSHEY_COMPLEX,
               1, (255, 0, 0), 3)

    cv.imshow("Img", img)
    cv.waitKey(1)