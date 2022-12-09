import cv2 as cv
import numpy as np
# import os

# os.chdir('Geometri/')

img = cv.imread('./sample.jpg')
# sample = [
#     [1, 0, 0, 0, 1],
#     [1, 1, 0, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1]
# ]

# sample = np.array(sample)

# print(img)0
sample = cv.resize(img, (600, 500), interpolation=cv.INTER_AREA)

# sample = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

translationX = -100
translationY = -300

imgRow = len(sample)
imgCol = len(sample[0])
imgCh = len(sample[0, 0])

imgTrans = np.zeros((imgRow, imgCol, imgCh))
imgTrans = imgTrans.astype(np.uint8)

for row in range(imgRow):
    for col in range(imgCol):
         for ch in range(imgCh) :
            newRow = row + translationX
            newCol = col + translationY

            if 0 < newRow < imgRow and 0 < newCol < imgCol:
                imgTrans[newRow, newCol, ch] = sample[row, col, ch]

# print(imgCh)
# print()
# print(imgTrans[:, :])
cv.imshow('sample', sample)
cv.imshow('result', imgTrans)
cv.waitKey(0)
cv.destroyAllWindows()
