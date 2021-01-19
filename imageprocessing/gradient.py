import cv2
import numpy as np
im=cv2.imread('image/pussi.png')
img=cv2.resize(im,(400,390))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#_,thresh=cv2.threshold(gray,130,250,cv2.THRESH_BINARY)
thresh=cv2.adaptiveThreshold(gray,250,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,3)

#gradient
dx,dy=cv2.spatialGradient(thresh)
sob1=cv2.Sobel(img,-1,1,0)
sob2=cv2.Sobel(img,-1,0,1)
lap=cv2.Laplacian(img,-1)
shrX=cv2.Scharr(img,-1,1,0)
shrY=cv2.Scharr(img,-1,0,1)
#totlacol=cv2.bitwise_and()
stk1=np.hstack((sob1,sob2))
stk2=np.hstack((shrX,shrY))
stk3=np.vstack((stk1,stk2))
cv2.imshow("output",stk3)
#cv2.imshow("original",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()