# import cv2 as cv
# import numpy as np
# import os

# os.chdir('Geometri/')

# img = cv.imread('a.jpg')

# # print(img)
# sample = cv.resize(img, (4, 5), interpolation=cv.INTER_AREA)

# sample = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

# translationX = 1
# translationY = 0

# imgRow = len(sample)
# imgCol = len(sample[0])

# imgTrans = np.zeros((imgRow, imgCol))

# imgTrans = imgTrans.astype(np.uint8)

# for row in range(imgRow):
#     for col in range(imgCol):
        

# print(sample[:,:])
# print(imgTrans[:,:])
# cv.imshow('sample', imgTrans)
# cv.waitKey(0)
# cv.destroyAllWindows()