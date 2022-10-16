import cv2 as cv
import numpy as np

sample = cv.imread('./sample.jpg')
img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

row_len = len(img)
col_len = len(img[0])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

treshold = 150

img_bin = gray

for row in range(row_len):
    for col in range(col_len):
        pixel = gray[row, col]
        if pixel > treshold:
            img_bin[row, col] = 255
        else:
            img_bin[row, col] = 0

cv.imshow('sample', img_bin)
# cv.imshow('sample - b', b)

cv.waitKey(0)
cv.destroyAllWindows()