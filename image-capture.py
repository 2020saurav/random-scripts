#!/usr/bin/env python
import cv2
import time
from PIL import Image

cam = cv2.VideoCapture(0)
cv2.namedWindow("WebCam")

def get_image():
	retval, im = cam.read()
	return im

fil = "/home/saurav/Pictures/webcam/"+str(time.asctime(time.localtime(time.time())))+".jpg"
camera_capture = get_image()
cv2.imwrite(fil,camera_capture)
img = Image.open(fil)
img.show()
del(cam)