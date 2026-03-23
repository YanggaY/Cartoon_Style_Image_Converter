import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('image.jpg')

# 이미지 로드 실패시 종료
if img is None:
    print("Can't load the image")
    exit()

# 이미지를 Grayscale로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)

# Canny edge detector로 윤곽선(Edges) 검출
edges = cv.Canny(gray, 70, 130)

kernel = np.ones((2,2), np.uint8)

# dilation으로 윤곽선 두껍게
edges = cv.dilate(edges, kernel, iterations=2)

# bilateral filter를 사용하여 edge는 구분하며 디테일을 뭉갬
color = cv.bilateralFilter(img, 9, 200, 200)

cartoon = color.copy()

# 윤곽선이 있는 부분을 검정색으로 덮어쓰기
cartoon[edges != 0] = (0,0,0)

# 원본이미지 출력
cv.imshow('Original', img)

# 만화스타일 이미지 출력
cv.imshow('Cartoon', cartoon)

cv.waitKey(0)
cv.destroyAllWindows()

