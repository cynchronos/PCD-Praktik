import cv2 as cv
import numpy as np

sample = cv.imread('../sample.jpg')

img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

img_row = len(img)
img_col = len(img[0])

gray = np.zeros((img_row, img_col))
# loop row and cols basic
for row in range(img_row):
    for col in range(img_col):
        # worst grayscale
        # gray[row, col] = round((r[row, col] + g[row, col] + b[row, col]) / 3)
        # best grayscale
        gray[row, col] = round(0.299 * r[row, col] + 0.587 * g[row, col] + 0.114 * b[row, col])

gray = gray.astype(np.uint8)


cv.imshow('sample', gray)
# cv.imshow('sample - b', b)

cv.waitKey(0)
cv.destroyAllWindows()
