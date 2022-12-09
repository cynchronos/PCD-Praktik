import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

sample = cv.imread('./sample.jpg')

img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

# Convert to Grayscale
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# save amount of row and column
row_len = len(img)
col_len = len(img[0])

cv.imshow('sample', img)
cv.waitKey()