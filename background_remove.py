import numpy as np
import cv2

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M2-pic.jpg")
img = cv2.resize(img,(800,800))
mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1,65), np.float64)*255
fgdmodel = np.zeros((1,65), np.float64)*255

rect = (134,150,660,730)
cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 5, cv2.GC_INIT_WITH_RECT)


mask2 = np.where((mask == 2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]


cv2.imshow("res==",img)
cv2.waitKey()
cv2.destroyAllWindows()