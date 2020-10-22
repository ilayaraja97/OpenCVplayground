import cv2 as cv
import numpy as np

cap = cv.VideoCapture("http://192.168.1.120:4747/video")
cv.namedWindow('image')

_,prev_frame = cap.read()
prev_frame=cv.cvtColor(prev_frame,cv.COLOR_BGR2GRAY)
sub_model=cv.createBackgroundSubtractorMOG2(history=500,varThreshold=400) # createBackgroundSubtractorKNN()
sub_model_mask=cv.createBackgroundSubtractorMOG2()

while(1):
    # Take each frame
    _, img = cap.read()
    if img is None:
        break
    # img=cv.resize(img,(800,600))
    # img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    mask=sub_model.apply(img)
    mask=sub_model_mask.apply(mask)
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('image',res)
    prev_frame=img
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
