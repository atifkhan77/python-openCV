import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
print(cap.isOpened())
while (cap.isOpened):
    ret, frame  = cap.read()# reading frame
    if ret==True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: '+ str(cap.get(4))# adding text to video 
        datet = str(datetime.datetime.now()) #adding date and time to video 
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        out.write(frame)
       

        cv2.imshow('frame',frame) #creating frame for video which pops up when code is executed

        if cv2.waitKey(1) & 0xFF == ord('q'):# frame will close when 'q' is pressed 
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()