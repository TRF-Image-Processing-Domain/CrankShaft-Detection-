import cv2
import numpy as np
# Load an image
image = cv2.imread('images/1.jpeg')
frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# masking
bgrl = np.array([42, 0, 0])  # black
bgrh = np.array([255, 48, 77])  # black
mask = cv2.inRange(frame, bgrl, bgrh)
# image clearing techniques
kernel = np.ones((2, 2), np.uint8)
morph = cv2.morphologyEx(mask, cv2.MORPH_OPEN, 	kernel)
blur = cv2.dilate(morph, kernel, iterations=2)

cv2.imshow('masked', blur)
# Find Contours
contours, _ = cv2.findContours(blur, cv2.RETR_TREE, 	cv2.CHAIN_APPROX_SIMPLE)
# print("Total number of contours : ", len(contours))
count = 0
for i in contours:
	area = cv2.contourArea(i)
	# print(i)
	# print(area)
	# finding best contour
	if area > 395:
		count += 1
		cv2.drawContours(image, i, -1, (0, 230, 0), 2)
		x, y, w, h = cv2.boundingRect(i)
		cv2.rectangle(image, (x, y), (x+40, y+50), (0, 255, 255), 2)

print("Number of contours with marked rectangle : ", 		count)

cv2.namedWindow('Contours', 		cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Contours', 		cv2.WND_PROP_FULLSCREEN, 		cv2.WINDOW_FULLSCREEN)

cv2.imshow('Contours', image)
cv2.waitKey(0)