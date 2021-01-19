import cv2

cam=cv2.VideoCapture(0)
print(cam.isOpened)
while cam.isOpened():
   _,frame=cam.read()
   flipped=cv2.flip(frame,1)
   #dst1=cv2.stylization(flipped)
   
   #dst3=cv2.bilateralFilter(flipped,-1,1,1)
   #dst4,dst5=cv2.pencilSketch(flipped)
   dst13=cv2.filter2D(flipped,-1,(1,1))
   #dst7=cv2.sepFilter2D(flipped,-1,1,1)
   dst9=cv2.detailEnhance(dst13)
   #dst10=cv2.boxFilter(dst9,-1,(1,1))
   dst2=cv2.edgePreservingFilter(dst9)

   #dst12=cv2.pyrMeanShiftFiltering(flipped,2,2)
   
   
   cv2.imshow("output",dst2)
   key=cv2.waitKey(1)
   if key==27:
    	break

cam.release()
   
