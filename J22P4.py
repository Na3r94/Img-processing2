import cv2

img = cv2.imread('chess pieces.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img.shape)

for i in range(7):
    a = img[0:275, 0 + i*80 + 3*i :79 + i*79 + 6*i]
    cv2.imwrite(f'Chess Pieces{i}.jpg',a)
cv2.imshow('Output', a)
cv2.waitKey()