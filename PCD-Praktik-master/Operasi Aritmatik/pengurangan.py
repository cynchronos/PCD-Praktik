import cv2 as cv
import numpy as np
import os

# os.chdir("/mnt/01D8CC470068EB90/Github/PCD-Praktik/Operasi Aritmatik/")

img1 = cv.imread("person.jpg")
img2 = cv.imread("sample2.jpg")

sample1 = cv.resize(img1, (500, 500))
sample2 = cv.resize(img2, (500, 500))

img_row = len(sample1)
img_col = len(sample1[0])
img_chn = len(sample1[0, 0])

newImage = np.zeros((img_row, img_col, img_chn))
newImage = newImage.astype(np.uint8)

medium = img2

for row in range(img_row):
    for col in range(img_col):
        for chn in range(img_chn):
            pixel = sample1[row, col, chn] - sample2[row, col, chn]
            
            if pixel < 1 :
                newImage[row, col, chn] = 0
            else:
                newImage[row, col, chn] = pixel

# print(newImage[0, :, 0])
# cv.imshow('sample1', sample1)
cv.imshow('result', newImage)
cv.waitKey(0)
