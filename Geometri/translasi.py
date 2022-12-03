import cv2 as cv
import numpy as np
import os

os.chdir('Geometri/')

img = cv.imread('a.jpg')
# sample = [
#     [1, 0, 0, 0, 1],
#     [1, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1]
# ]

# sample = np.array(sample)

# print(img)
sample = cv.resize(img, (5, 5), interpolation=cv.INTER_AREA)

sample = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

translationX = 3
translationY = -2

imgRow = len(sample)
imgCol = len(sample[0])

imgTrans = np.zeros((imgRow, imgCol))
imgTrans = imgTrans.astype(np.uint8)

for row in range(imgRow):
    for col in range(imgCol):
        newRow = row + translationX
        newCol = col + translationY

        if 0 < newRow < imgRow and 0 < newCol < imgCol:
            imgTrans[newRow, newCol] = sample[row, col]

print(sample[:, :])
print()
print(imgTrans[:, :])
# cv.imshow('sample', imgTrans)
# cv.waitKey(0)
# cv.destroyAllWindows()
