import numpy as np
import cv2 as cv
def nothing(x):
    pass
# Create a black image, a window
img = cv.imread(cv.samples.findFile("images/map.png"))
img = cv.resize(img,None,fx=0.75, fy=0.75, interpolation = cv.INTER_AREA)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('X','image',0,2000,nothing)
cv.createTrackbar('Y','image',0,2000,nothing)
cv.createTrackbar('R','image',0,2000,nothing)
show=np.copy(img)
while(1):
    cv.imshow('image',show)
    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc
        break
    # get current positions of four trackbars
    x = cv.getTrackbarPos('X','image')
    y = cv.getTrackbarPos('Y','image')
    r = cv.getTrackbarPos('R','image')
    show=np.copy(img)
    cv.circle(show,(x,y), r, (0,0,255))
cv.destroyAllWindows()