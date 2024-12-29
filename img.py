import cv2

img1 = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M-pic.jpg", -1)

img1 = cv2.resize(img1,(1280,700))

img1 = cv2.flip(img1,0)
cv2.imshow("converted image==", img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("x"):
    cv2.destrotAllwindows()
elif k == ord("w"):
    cv2.imwrite("hehe.png".img1)
    cv2.destroyAllwindows()
    
    