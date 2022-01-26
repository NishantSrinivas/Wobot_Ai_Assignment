import cv2 as cv
from pyzbar.pyzbar import decode

image = cv.imread("QR2.jpg")
#image = cv.imread("mom.png")
data  = decode(image)

print(data[0][0])