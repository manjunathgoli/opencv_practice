import cv2
import datetime

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("width==>",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height==>",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1280)
cap.set(4,720)


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        frame = cv2.flip(frame,2)
        text = ' height: ' + str(cap.get(4)) + 'Width:' + str(cap.get(3))
        date =  'Date: ' + str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,20), font, 1,(0,155,255),1)
        
        frame = cv2.putText(frame, date, (20,50), font, 1, (100,255,255), 1)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
            
    else:
        break

cap.release()
cv2.destroyAllWindows()