'''
cascade(object) dection......
1. import cascade.xml files
2. find cascade cordinate -> detectmultiscale() method
3. draw rectangle for those cordinate
4. for cascade eye detection better to input crop gray face and output crop color face
5. input and out put image should be of same size for draw rectangle

'''
import cv2
import numpy as np
cam=cv2.VideoCapture(0)
#importing cascade file
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('cascades/haarcascade_smile.xml')
#hand_dector=cv2.CascadeClassifier("")

while cam.isOpened():
	#next frame
	red,frame=cam.read()
	#flip image
	flipped=cv2.flip(frame,1)
	#gray
	img_gray=cv2.cvtColor(flipped,6)
	#face
	
	face_cordinate=face_cascade.detectMultiScale(img_gray, 1.1, 33)
	for (x, y, w, h) in face_cordinate:
	    cv2.rectangle(flipped,(x,y),((x+w),(y+h)),(255,0,0),3)
	#crop face
	    face_gray_crop=img_gray[y:y+h,x:x+w]
	    face_color_crop=flipped[y:y+h,x:x+w]
	#eye
	    eye_cordinate=eye_cascade.detectMultiScale(face_gray_crop, 1.1, 22)
	    for (x,y,w,h) in eye_cordinate:
	        cv2.rectangle(face_color_crop,(x,y),((x+w),(y+h)),(0,0,255),2)
	        	
	#smile
	    smile_cordinate=smile_cascade.detectMultiScale(face_gray_crop,1.6,22)
	    for (x,y,w,h) in smile_cordinate:
	        cv2.rectangle(face_color_crop,(x,y),((x+w),(y+h)),(0,255,0),2)  
	    break 
	           
	#show
	cv2.imshow("output",flipped)

	
	#key event for exit
	key=cv2.waitKey(1)

	if key==27 or 0xFF == ord('q'):
         break
cam.release()         
    
	


	