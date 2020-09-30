import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images/samidha.jpg",cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(300,300), interpolation = cv.INTER_AREA)

rows,cols = img.shape
pts1 = np.float32([[114,73],[231,94],[114,168],[190,168]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.gray()
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()