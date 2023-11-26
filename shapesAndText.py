import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)

#coloring the image blue:
#img[200:300,150:350] = 255,0,0

#drawing a green line on image: you can give height and width but as we are going to end the img,shape[0] and [1] property is used for start to ending
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)

#for rectangle:
cv2.rectangle(img,(10,10),(250,350),(0,255,255),2)

#for circle:
cv2.circle(img,(400,50),30,(255,255,0),4)

#for text:
cv2.putText(img," OpenCv ",(300,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("image",img)
cv2.waitKey(0)