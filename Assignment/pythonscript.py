import numpy as np
import imutils
import cv2
image = cv2.imread("mark.jpg")
for angle in np.arange(0, 360,0.5):
	rotated = imutils.rotate(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.imwrite("img"+str(angle)+".jpg",rotated)
	cv2.waitKey(1)
