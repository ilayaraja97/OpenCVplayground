import cv2 as cv
import numpy as np
import argparse

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

cap = cv.VideoCapture(args.source)
# cv.namedWindow('mask')
cv.namedWindow('res')

def get_k_frames(k=5):
    p=[]
    for i in range(k):
        _,f = cap.read()
        f=cv.cvtColor(f,cv.COLOR_BGR2GRAY)
        p.extend([f])
    p=np.array(p)
    return p

kframes=get_k_frames(k=args.frames)

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
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('res',res)
    # pop_front() & push_back()
    kframes=np.append(kframes[1:],[grey],axis=0)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()