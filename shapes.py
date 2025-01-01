import cv2 # type: ignore
import numpy

img = cv2.imread(r"C:\Users\JOHNPAUL\Desktop\manju\linkedin\M-pic.jpg")
img = cv2.resize(img,(400,500))
overlay = img.copy()

# img = cv2.line(img, (0,0), (200,200), (0,0,0), 4)

# img = cv2.arrowedLine(img, (0,0), (200,200), (0,0,0), 4)

img = cv2.rectangle(img, (0,0), (200,200), (255,255,255), 5)

# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, "manju manjunath", (20,85), font, 4, (0,0,0), 3, cv2.LINE_4)
alpha = 1  # Transparency factor
img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

cv2.imshow("line img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()