import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):
    pass

cap = cv.VideoCapture("http://192.168.1.4:4747/video")
cv.namedWindow('image')
cv.createTrackbar('X1','image',0,399,nothing)
cv.createTrackbar('X2','image',0,399,nothing)
while(1):
    # Take each frame
    _, img = cap.read()
    if img is None:
        break
    img=cv.resize(img,(800,600))
    x1 = cv.getTrackbarPos('X1','image')
    x2 = cv.getTrackbarPos('X2','image')
    pts1 = np.float32([[x1,0],[800-x1,0],[x2,600],[800-x2,600]])
    pts2 = np.float32([[0,0],[800,0],[0,600],[800,600]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(800,600))
    cv.imshow('image',dst)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
