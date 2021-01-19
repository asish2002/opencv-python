import cv2
girlimg=cv2.imread('image/pussi.png')
hsv=cv2.cvtColor(girlimg,cv2.COLOR_BGR2HSV)
gray=cv2.cvtColor(girlimg,cv2.COLOR_BGR2GRAY)
cv2.imshow("output",girlimg)

def change(a):
    higher=(cv2.getTrackbarPos("blue","output"),cv2.getTrackbarPos("green","output"),cv2.getTrackbarPos("red","output"))
    lower=(0,0,0)
    mask=cv2.inRange(hsv,lower,higher)
    col_msk=cv2.bitwise_and(girlimg,girlimg,mask=mask)    
    cv2.imshow("output",mask)

cv2.createTrackbar("blue","output",0,255,change)
cv2.createTrackbar("green","output",0,255,change)
cv2.createTrackbar("red","output",0,255,change)
cv2.waitKey(0)
cv2.destroyAllWindows()
