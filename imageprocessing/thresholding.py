import cv2
pic1=cv2.imread('image/pussi.png')
gray=cv2.cvtColor(pic1,cv2.COLOR_BGR2GRAY)
cv2.imshow("globalthreshold",gray)
cv2.imshow("adaptiveThreshold",gray)

def update(a):
	val1=cv2.getTrackbarPos("Threshold1","globalthreshold")
	val2=cv2.getTrackbarPos("Threshold2","globalthreshold")
	j=cv2.getTrackbarPos("Therstype","globalthreshold")
	b=[cv2.THRESH_BINARY,cv2.THRESH_MASK,cv2.THRESH_OTSU,cv2.THRESH_TOZERO,cv2.THRESH_TRIANGLE,cv2.THRESH_TRUNC,cv2.THRESH_BINARY_INV,cv2.THRESH_TOZERO_INV]
	_,thres1=cv2.threshold(gray,val1,val2,b[j])
	_,thres2=cv2.threshold(gray,val1,val2,b[j])
	
	cv2.imshow("globalthreshold",thres1)
	

def adptThres(b):
	maxval=cv2.getTrackbarPos("maxvalue","adaptiveThreshold")
	i=cv2.getTrackbarPos("adaptType","adaptiveThreshold")
	j=cv2.getTrackbarPos("adTherstype","adaptiveThreshold")
	cons=cv2.getTrackbarPos("constant","adaptiveThreshold")
	a=[cv2.ADAPTIVE_THRESH_MEAN_C,cv2.ADAPTIVE_THRESH_GAUSSIAN_C]
	b=[cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV]
	adapth=cv2.adaptiveThreshold(gray,maxval,a[i],b[j],13,cons)	
	cv2.imshow("adaptiveThreshold",adapth)

cv2.createTrackbar("Threshold1","globalthreshold",0,255,update)
cv2.createTrackbar("Threshold2","globalthreshold",0,255,update)
cv2.createTrackbar("Therstype","globalthreshold",0,7,update)
cv2.createTrackbar("maxvalue","adaptiveThreshold",0,255,adptThres)
cv2.createTrackbar("constant","adaptiveThreshold",0,255,adptThres)
cv2.createTrackbar("adaptType","adaptiveThreshold",0,1,adptThres)
cv2.createTrackbar("adTherstype","adaptiveThreshold",0,1,adptThres)


cv2.waitKey(0)
cv2.destroyAllWindows()