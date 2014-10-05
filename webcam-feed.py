#!/usr/bin/env python
import cv2

cv2.namedWindow("Lookback")

vc = cv2.VideoCapture(0)

if vc.isOpened():
	rval, frame = vc.read()
else:
	rval = False

while rval:
	cv2.imshow("Lookback", frame)
	rval, frame = vc.read()
	key = cv2.waitKey(1)
	if key != -1:
		break
cv2.destroyAllWindows()