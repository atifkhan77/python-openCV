import cv2
import numpy as np

#original image
img = cv2.imread('resources/lambo.jpg')
print(img.shape)
cv2.imshow('Image',img)

#resizing image:
imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)
cv2.imshow('Resize Image',imgResize)

#crop image:
imgCrop = img[0:300,0:400]
cv2.imshow('Crop Image',imgCrop)


cv2.waitKey(0)