import cv2

img_org = cv2.imread('board - origin.bmp')
img_test = cv2.imread('board - test.bmp')
img_org = cv2.cvtColor(img_org, cv2.COLOR_RGB2GRAY)
img_test = cv2.cvtColor(img_test, cv2.COLOR_RGB2GRAY)
img_test = cv2.flip(img_test, 1)

img_result = cv2.subtract(img_test, img_org) *2

cv2.imshow('Black Hole', img_result)
cv2.waitKey(0)