import cv2
cam=cv2.VideoCapture(0)

def look(b):
	pass
cv2.namedWindow("vision")
cv2.createTrackbar("brightness","vision",0,100,look)
def change(a):
	pass
cv2.namedWindow("out")
cv2.createTrackbar("blue","out",0,255,change)
cv2.createTrackbar("green","out",0,255,change)
cv2.createTrackbar("red","out",0,255,change)
cv2.createTrackbar("blueI","out",0,255,change)
cv2.createTrackbar("greenI","out",0,255,change)
cv2.createTrackbar("redI","out",0,255,change)
while cam.isOpened():
	bright=cv2.getTrackbarPos("brightness","vision")
	cam.set(10,bright)
	_,read=cam.read()
    
	flipped=cv2.flip(read,1)
	
	hsv=cv2.cvtColor(flipped,cv2.COLOR_BGR2HSV)
	
	#gausian_blur=cv2.adaptiveThreshold(hsv,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)
	mask=cv2.inRange(hsv,(cv2.getTrackbarPos("blueI","out"),cv2.getTrackbarPos("greenI","out"),cv2.getTrackbarPos("redI","out")),(cv2.getTrackbarPos("blue","out"),cv2.getTrackbarPos("green","out"),cv2.getTrackbarPos("red","out")))
	col_mas=cv2.bitwise_and(flipped,flipped,mask=mask)
	gray=cv2.cvtColor(col_mas,cv2.COLOR_BGR2GRAY)
	_,thres=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
	#contour,her=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	#draw_con=cv2.drawContours(col_mas,contour,-1,(0,255,0),3)

	cv2.imshow("output",col_mas)
	
    
   
	key=cv2.waitKey(1)
	if key==27:
		break
cam.release()		