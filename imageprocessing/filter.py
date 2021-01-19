import cv2
import numpy as np

im=cv2.imread('image/pussi.png')
img=cv2.resize(im,(400,300))

dst1=cv2.stylization(img)
dst2=cv2.edgePreservingFilter(img)
dst3=cv2.bilateralFilter(img,-1,1,1)
dst4,dst5=cv2.pencilSketch(img)
#dst6=cv2.sqrBoxFilter(img,-1,(1,1))
dst7=cv2.sepFilter2D(img,-1,1,1)
#dst8=cv2.filterSpeckles(img,1,1,1)
dst9=cv2.detailEnhance(img)
dst10=cv2.boxFilter(img,-1,(1,1))

#dst11=cv2.filterHomographyDecompByVisibleRefpoints()
dst12=cv2.pyrMeanShiftFiltering(img,2,2)
dst13=cv2.filter2D(img,-1,(1,1))




stk1=np.hstack((dst1,dst2,dst3,dst7))
stk2=np.hstack((dst9,dst10,dst12,dst13))
stk3=np.vstack((stk1,stk2))

cv2.imshow("output1",stk3)
cv2.imshow("output2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()