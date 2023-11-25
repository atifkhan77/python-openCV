import cv2
import numpy as np


img  = cv2.imread('resources/mine.jpeg')
kernal = np.ones((5,5),np.uint8)
#for Converting image to gray:
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#for Converting image to Blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#for showing edges:
imgCanny = cv2.Canny(img,150,200)
#dialation image:
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
#image Eroded:opposite of dialation
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow('Gray Image',imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Canny Image',imgCanny)

cv2.imshow('Dialation Image',imgDialation)

cv2.imshow('Eroded Image',imgEroded)

cv2.waitKey(0)