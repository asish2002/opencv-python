import cv2

Tamp=cv2.imread("image/girleye.png")
grayT=cv2.cvtColor(Tamp,cv2.COLOR_BGR2GRAY)
h,w = Tamp.shape[:2]
print(w,',',h)
cv2.imshow("TemplateImage",Tamp)
cv2.waitKey(0)
cv2.destroyAllWindows()

Original=cv2.imread("image/girl.png")
cv2.imshow("OriginalImage",Original)
grayO=cv2.cvtColor(Original,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()

res1=cv2.matchTemplate(grayO,grayT,cv2.TM_SQDIFF)
min1Val,max1Val,min1Loc,max1Loc=cv2.minMaxLoc(res1)
print(min1Val,',',max1Val,',',min1Loc,',',max1Loc)
topleft=min1Loc
btmRht=(topleft[0]+h,topleft[1]+w)
print(res1)
cv2.rectangle(Original,topleft,btmRht ,(0,255,0))
cv2.imshow("HERE IS MATCHING",Original)
cv2.waitKey(0)
cv2.destroyAllWindows()