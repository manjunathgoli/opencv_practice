import cv2
import numpy as np

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M-pic.jpg")
img = cv2.resize(img, (600,600))

pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)
pu1 = cv2.pyrUp(pd2)

cv2.imshow("og_img",img)
cv2.imshow("pd1==>",pd1)
cv2.imshow("pd2==>",pd2)
cv2.imshow("pu1==>",pu1)

cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = img.copy()
data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow('res',img1)

cv2.imshow('og_img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()