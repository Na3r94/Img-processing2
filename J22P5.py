import cv2
import numpy as np

images=[]
for i in range(0,15):
    img = cv2.imread(f'highway/h{i}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    images.append(img)

img_result = np.zeros(images[0].shape, dtype='uint8')

for image in images:
    img_result += image // len(images)

cv2.imwrite('Highway.jpg', img_result)
cv2.imshow('Highway', img_result)
cv2.waitKey(0)