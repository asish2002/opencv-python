import cv2
import numpy as np
img=cv2.imread('image/corner.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gra=cv2.equalizeHist(gray)
th=cv2.adaptiveThreshold(gra,250,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
er=cv2.erode(th,(10,10))
#grayC=clah.apply(gray)
gflo32=np.float32(er)
dst=cv2.cornerHarris(er,3,9,0.0010)

img[dst>34]=[0,0,255]
#img[0]=[0,0,255]
#img[img>28]
print(dst>34)
cv2.imshow('dst',img)
cv2.waitKey(0)
