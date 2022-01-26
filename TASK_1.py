from ast import increment_lineno


import cv2 as cv
image = cv.imread('snap.jpg')
edges = cv.Canny(image,200,100)
cv.imshow("snap_edges",edges)
cv.waitKey(0)