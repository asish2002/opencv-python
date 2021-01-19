import cv2
import numpy as np
img=cv2.imread("image/line.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres=cv2.threshold(gray,210,255,cv2.THRESH_BINARY)
can=cv2.Canny(thres,100,250,3)
'''
lines=cv2.HoughLines(can,12,np.pi,30)
#print(lines)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("output",img)
'''
prol=cv2.HoughLinesP(can,1,1,1)
print(prol)
for x1,y1,x2,y2 in prol[0]:
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("out",img)
cv2.waitKey(0)