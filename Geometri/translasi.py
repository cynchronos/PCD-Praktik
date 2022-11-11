from pickletools import uint8
import cv2 as cv
import numpy as np

img = cv.imread('./sample.jpg')

# print(img)
sample = cv.resize(img, (852, 480), interpolation=cv.INTER_AREA)

translationX = -300

imgRow = len(sample)
imgCol = len(sample[0])
imgChn = len(sample[0,0])

imgTrans = np.zeros((imgRow, imgCol, imgChn))

imgTrans = imgTrans.astype(np.uint8)

for row in range(imgRow):
    for col in range(imgCol):
        for chn in range(imgChn):
            newCol =  (img + translationX)
            imgTrans[row, newCol, chn] = sample[row, col, chn]
        
cv.imshow('sample', imgTrans)
cv.waitKey(0)
cv.destroyAllWindows()