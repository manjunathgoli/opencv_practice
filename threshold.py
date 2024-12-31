import cv2
import numpy as np

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M2-pic.jpg")
img = cv2.resize(img,(300,300))
cv2.imshow("og_img", img)

# SIMPLE THRESHOLD

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow("1- BINARY", th1)
cv2.imshow("1- BINARY_INV", th2)
cv2.imshow("1- THRESH_TRUNC", th3)
cv2.imshow("1- TOZERO", th4)
cv2.imshow("1- TOZERO_INV", th5)


# ADAPTIVE THRESHOLD

th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY)
th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY)

cv2.imshow("og_img", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN", th6)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_c", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()