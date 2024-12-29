import cv2

cap = cv2.VideoCapture(r"C:\Users\JOHNPAUL\Videos\database.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("nor-col",frame)
    cv2.imshow("gray-vid",gray)
    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("check",cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame= cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        gray = cv2.flip(gray,2)
        output.write(gray)
        
        cv2.imshow("gray",gray)
        cv2.imshow("color",frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    else:
        break
    
cap.release()
output.release()
cv2.destroyAllWindows()