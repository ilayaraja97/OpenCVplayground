#%% import
import cv2 as cv
import numpy as np
# %% color space flags
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)


# %% track blue green red object
cap = cv.VideoCapture("http://192.168.1.120:4747/video")

while(1):
    # Take each frame
    _, frame = cap.read()
    if frame is None:
        break
    frame=cv.resize(frame,(800,600))
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # define range of red color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    # define range of green color in HSV
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])
    # Threshold the HSV image to get only certain colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    # Merge masks
    mask=mask_red
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
# %%
