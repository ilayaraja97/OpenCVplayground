import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global mode,drawing,ix,iy
    if event == cv.EVENT_LBUTTONDOWN:
        drawing=True
        (ix,iy)=(-1,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing=False
    if drawing and event == cv.EVENT_MOUSEMOVE:
        if((ix,iy)==(-1,-1)):
            (ix,iy)=(x,y)
        cv.line(img,(ix,iy),(x,y),0xFFFFFF)
        (ix,iy)=(x,y)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1)
    if  k == ord("q"):
        break
cv.destroyAllWindows()