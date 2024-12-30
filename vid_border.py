import cv2
import numpy as np

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M-pic.jpg")
img = cv2.resize(img,(400,400))

img_brdr = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT, value = [0,0,125])

cv2.imshow("borderd_img", img_brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()