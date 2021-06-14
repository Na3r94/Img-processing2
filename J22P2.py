import cv2
import numpy
import numpy as np

def noise(num):
    images=[]
    for i in range(1,6):
        img = cv2.imread(f'black hole/{num}/{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        images.append(img)

    img_result = np.zeros(images[0].shape, dtype='uint8')

    for image in images:
        img_result += image // len(images)

    cv2.imwrite(f'result{num}.jpg', img_result)

noise(1)
noise(2)
noise(3)
noise(4)

img1 = cv2.imread('result1.jpg')
img2 = cv2.imread('result2.jpg')
img3 = cv2.imread('result3.jpg')
img4 = cv2.imread('result4.jpg')

v_img = cv2.vconcat([img1, img3])
v_img2 = cv2.vconcat([img2, img4])
img = cv2.hconcat([v_img, v_img2])
cv2.imwrite('Black Hole.jpg', img)
cv2.imshow('Black Hole', img)
cv2.waitKey(0)