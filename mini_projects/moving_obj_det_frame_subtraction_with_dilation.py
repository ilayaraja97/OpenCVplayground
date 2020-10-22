import cv2 as cv
import numpy as np
import argparse
import random as rng
rng.seed(12345)

parser = argparse.ArgumentParser(description='Capture moving objects.')
parser.add_argument('--frames',dest='frames', metavar='k', type=int, nargs='?',
                    help='number of frames to be averaged',default=4)
parser.add_argument('--threshold',dest='threshold', metavar='threshold', type=int, nargs='?',
                    help='pixel difference threshold',default=20)
parser.add_argument('--source',dest='source', metavar='source', type=str, nargs='?',
                    help='source of video',default="http://192.168.1.120:4747/video")

args = parser.parse_args()

threshold=args.threshold
if args.source.isnumeric():
    args.source=int(args.source)

def nothing(x):
    pass

def dilatation(src, dilatation_size, val_type):
    dilatation_type = 0
    if val_type == 0:
        dilatation_type = cv.MORPH_RECT
    elif val_type == 1:
        dilatation_type = cv.MORPH_CROSS
    elif val_type == 2:
        dilatation_type = cv.MORPH_ELLIPSE
    element = cv.getStructuringElement(dilatation_type, (2*dilatation_size + 1, 2*dilatation_size+1), (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)
    return dilatation_dst

# cv.namedWindow('mask')
cv.namedWindow('res')
def get_k_frames(k=5):
    p=[]
    for _ in range(k):
        _,f = cap.read()
        f=cv.cvtColor(f,cv.COLOR_BGR2GRAY)
        p.extend([f])
    p=np.array(p)
    return p
try:
    cap = cv.VideoCapture(args.source)
    kframes=get_k_frames(k=args.frames)
except Exception as e:
    # print(e)
    print("Video not connected")

while(1):
    # Take each frame
    _, img = cap.read()
    if img is None:
        break
    grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    avg=np.average(kframes,axis=0).astype(np.uint8)
    mask=cv.absdiff(grey,avg)
    mask[mask>=threshold]=255
    mask[mask<threshold]=0
    # cv.imshow('mask',mask)
    mask=dilatation(mask,20,2)
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('res',res)
    # pop_front() & push_back()
    kframes=np.append(kframes[1:],[grey],axis=0)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows() 