import cv2 as cv
import numpy as np

sample = cv.imread('./sample.jpg')

img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

# Display image matrix
# print(img[:,:,0])
# note : array [:,:] = display rows and columns, 0 = rgb(bgr in python) index 

# Display image B/G/R Only
# cv.imshow('sample', img[:,:,0])
# cv.imshow('sample1', img[:,:,1])
# cv.imshow('sample2', img[:,:,2])

# Convert to Grayscale
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# save amount of row and column
row_len = len(img)
col_len = len(img[0])

# Noob Convert/Mathematical
img_gray = np.zeros((row_len, col_len))
for row in range(row_len):
    for col in range(col_len):
        img_gray[row, col] = round(0.299 * r[row, col] + 0.587 * g[row, col] + 0.114 * b[row, col])

# Convert integer from array to unsigned integer for remove bug on image
img_gray = img_gray.astype(np.uint8)

# Pro Convert
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('sample', img_gray)

# cv.imshow('sample', img)
cv.waitKey(0)
cv.destroyAllWindows()
