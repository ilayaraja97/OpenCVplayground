import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px

cv.imshow("Display window", img)

k = ""
while(k!=ord("e")):
    k = cv.waitKey(0)
    if k == ord("1"):
        cv.line(img,(0,0),(511,511),(255,0,0),5)
    elif k==ord("2"):
        cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
    elif k==ord("3"):
        cv.circle(img,(447,63), 63, (0,0,255), -1)
    elif k==ord("4"):
        cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
    cv.imshow("Display window", img)