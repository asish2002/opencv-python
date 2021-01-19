import cv2
import numpy as np
im=cv2.imread('image/pussi.png')
img=cv2.resize(im,(350,260))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#_,thresh=cv2.threshold(gray,130,250,cv2.THRESH_BINARY)
thresh=cv2.adaptiveThreshold(gray,250,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,3)

#blur
blur1=cv2.blur(img,(1,1))
blur2=cv2.GaussianBlur(img,(1,1),1)
blur3=cv2.medianBlur(img,1)
stk1=np.hstack((blur1,blur2,blur3))
cv2.imshow("blur",stk1)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#morphology operation
mo1=cv2.erode(thresh,(1,1))
mo2=cv2.dilate(thresh,(1,1))
mo3=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,(1,1))
mo4=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,(1,1))
mo5=cv2.morphologyEx(thresh,cv2.MORPH_ELLIPSE,(1,1))
mo6=cv2.morphologyEx(thresh,cv2.MORPH_ERODE,(1,1))
mo7=cv2.morphologyEx(thresh,cv2.MORPH_RECT,(1,1))
mo8=cv2.morphologyEx(thresh,cv2.MORPH_DILATE,(1,1))
mo9=cv2.morphologyEx(thresh,cv2.MORPH_TOPHAT,(1,1))
mo10=cv2.morphologyEx(thresh,cv2.MORPH_BLACKHAT,(1,1))
mo11=cv2.morphologyEx(thresh,cv2.MORPH_GRADIENT,(1,1))
mo12=cv2.morphologyEx(thresh,cv2.MORPH_HITMISS,(-1,-1))

stk1=np.hstack((mo1,mo2,mo3,mo4))
stk2=np.hstack((mo5,mo6,mo7,mo8))
stk3=np.hstack((mo9,mo10,mo11,mo12))
stk4=np.vstack((stk1,stk2,stk3))
cv2.imshow("output",stk4)
cv2.imshow("original",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()



#denoise
#dns1=cv2.denoise_TVL1()
dns2=cv2.fastNlMeansDenoising(im)
dns3=cv2.fastNlMeansDenoisingColored(im)
#dns4=cv2.fastNlMeansDenoisingMulti()
#dns5=cv2.fastNlMeansDenoisingColoredMulti()
stk1=np.hstack((dns2,dns3))
cv2.imshow("denoise",stk1)
cv2.imshow("original",im)
cv2.waitKey(0)
cv2.destroyAllWindows()