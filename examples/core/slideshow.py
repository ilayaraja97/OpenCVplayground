import cv2 as cv
import sys

caged=cv.imread(cv.samples.findFile("caged.jpeg"))[0:300,0:300,0:3]
camera=cv.imread(cv.samples.findFile("camera.jpeg"))[0:300,0:300,0:3]

if caged is None:
    sys.exit("Could not read the caged image.")
if camera is None:
    sys.exit("Could not read the camera image.")
img = caged
cv.imshow("Slideshow",img)
# cv.waitKey(0)
x=0.0
mode=True
while(1):
    if(x>=1):
        mode=False
    elif x<=0:
        mode=True
    if mode:
        x=x+0.005
    else:
        x=x-0.005
    img=cv.addWeighted(caged,1-x,camera,x,0)
    cv.imshow("Slideshow",img)
    if cv.waitKey(20) & 0xFF == 27: 
        break
cv.destroyAllWindows()