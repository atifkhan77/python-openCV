import cv2
import numpy as np

img = cv2.imread('hello.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)

img = cv2.merge((b,g,r))

ball = img[402:462 , 452:512]
img[240:300 , 290:350] = ball



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()