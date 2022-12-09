import cv2 as cv
import numpy as np
import os

os.chdir('Geometri/')

img = cv.imread('./a.jpg')
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



imgRow = len(sample)
imgCol = len(sample[0])
imgCh = len(sample[0, 0])

imgFlip = np.zeros((imgRow, imgCol, 3))
imgFlip = imgFlip.astype(np.uint8)

vertical_flip = 0
horizontal_flip = 1
 
for row in range(imgRow):
    for col in range(imgCol):
        newrow = row
        newcol = col 
            
        if vertical_flip == 1 :
                newrow = imgRow - row - 1

        if horizontal_flip == 1:
                newcol = imgCol - col - 1

        imgFlip[newrow, newcol] = sample[row, col]

# print(imgCh)
# print()
# print(imgTrans[:, :])
cv.imshow('sample', sample)
cv.imshow('result', imgFlip)
cv.waitKey(0)
cv.destroyAllWindows()
