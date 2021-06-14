import cv2

img1 = cv2.imread('a.tif')
img2 = cv2.imread('b.tif')

img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

img_result = cv2.subtract(img2, img1)
rows, cols = img_result.shape
for i in range(rows):
    for j in range(cols):
        img_result[i,j] = 255 - img_result[i,j]

cv2.imshow('Output', img_result)
cv2.waitKey()