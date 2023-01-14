import cv2 as cv
import numpy as np
import os

os.chdir('Geometri/')

img = cv.imread('./a.jpg')

sample = cv.resize(img, (600, 500), interpolation=cv.INTER_AREA)

# sample = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

imgRow = len(sample)
imgCol = len(sample[0])

scale = 0.3

scaling_row = round(imgRow * scale)
scaling_col = round(imgCol * scale)

imgScale = np.zeros((scaling_row, scaling_col, 3))
imgScale = imgScale.astype(np.uint8)
 
for newRow in range(scaling_row):
    for newCol in range(scaling_col):
        row = int(newRow / scale)
        col = int(newCol / scale)
        
        imgScale[newRow, newCol] = sample[row, col]

# print(imgScale)
cv.imshow('sample', sample)
cv.imshow('result', imgScale)
cv.waitKey(0)
cv.destroyAllWindows()
