import cv2
import numpy as np

def click_event(events,x,y,flags,param):
    if events == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        pionts.append((x,y))
        if len(pionts)>=2:
            cv2.line(img,pionts[-1],pionts[-2],(255,0,0),5)
        cv2.imshow('image',img)
    
img = np.zeros((512,512,3),np.uint8)
#img = cv2.imread('hello.jpg')

cv2.imshow('image',img)
pionts = []
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()