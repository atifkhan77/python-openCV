import cv2
import numpy as np

img = cv2.imread('resources/cards.png')

width,height = 250,350


pts1 = np.float32([[38,301],[212,205],[110,429],[286,330]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
print(img.shape)
cv2.imshow('image',img)
cv2.imshow('image',imgOutput)

cv2.waitKey(0)
'''(303,38)
(205,212)
(429,110)
(330,286)'''