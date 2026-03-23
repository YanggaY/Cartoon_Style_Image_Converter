import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')

if img is None:
    print("Can't load the image")
    exit()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)

edges = cv.Canny(gray, 70, 130)


kernel = np.ones((2,2), np.uint8)
edges = cv.dilate(edges, kernel, iterations=2)

color = cv.bilateralFilter(img, 9, 200, 200)


cartoon = color.copy()
cartoon[edges != 0] = (0,0,0)


cv.imshow('Original', img)
cv.imshow('Cartoon', cartoon)

cv.waitKey(0)
cv.destroyAllWindows()

