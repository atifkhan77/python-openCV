import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
print(cap.isOpened())
while (cap.isOpened):
    ret, frame  = cap.read()# reading frame
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_Lab2BGR) # changing color of like filters

        cv2.imshow('frame',gray) #creating frame for video which pops up when code is executed

        if cv2.waitKey(1) & 0xFF == ord('q'):# frame will close when 'q' is pressed 
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()