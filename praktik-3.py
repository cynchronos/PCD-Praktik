from math import degrees
import cv2 as cv
import numpy as np

sample = cv.imread('../sample.jpg')
img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

color_degrees = 180

row_len = len(img)
col_len = len(img[0])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_bin = np.zeros((row_len, col_len))

for row in range(row_len):
    for col in range(col_len):
        if gray(row, col) >= degrees:
            img_bin[row, col] = 0
        else:
            img_bin[row, col] = 1

cv.imshow('sample', img_bin)
# cv.imshow('sample - b', b)

cv.waitKey(0)
cv.destroyAllWindows()