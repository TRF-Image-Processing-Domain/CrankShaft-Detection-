import cv2
	import numpy as np
	# Load an image
	image = cv2.imread('images/1.jpeg')

	# Changing the colour-space
	# blur = cv2.GaussianBlur(image, (3, 3), 0)
	blur = cv2.medianBlur(image, 11)
	frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	# Find edges

	bgrl = np.array([42, 0, 0])  # black
	bgrh = np.array([255, 40, 77])  # black

	# bgrl = np.array([62, 12, 46])  # shaft
	# bgrh = np.array([250, 255, 255])  # shaft
	mask = cv2.inRange(frame, bgrl, bgrh)

	cv2.imshow('masked', mask)
	# Find Contours
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, 	cv2.CHAIN_APPROX_SIMPLE)
	print("Total number of contours : ", len(contours))
	count = 0
	for i in contours:
   		area = cv2.contourArea(i)
   		# print(i)
   		# print(area)
   		if area > 350:
      		count += 1
      		cv2.drawContours(image, i, -1,(0, 230, 0),2)
      		x, y, w, h = cv2.boundingRect(i)
      		cv2.rectangle(image,(x, y),(w+x,
                 h+y),(0,255,255),2)
	print("Number of contours with marked rectangle : ", 	count)

	cv2.namedWindow('Contours', 	cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty('Contours', 	cv2.WND_PROP_FULLSCREEN, 	cv2.WINDOW_FULLSCREEN)

	cv2.imshow('Contours', image)
	cv2.waitKey(0)