import cv2
import numpy as np 

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M2-pic.jpg")
img = cv2.resize(img,(600,400))
cv2.imshow("ogimg",img)
print("shape", img.shape)
print("size", img.size)
print("data type", img.dtype)
print("img type", type(img))


# img split
b,g,r = cv2.split(img)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

# img merge
mr1 = cv2.merge((r,g,b))
cv2.imshow(mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow(mr2)
mr3 = cv2.merge((b,g,r))
cv2.imshow(mr3)

cv2.waitKey(0)
cv2.destroyAllWindows()
