import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import ndimage

os.chdir("Geometri/")
img = cv.imread('a.jpg')

sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sample = cv.resize(sample, (250, 350))

degree = -20

rotation = degree * np.pi/180

# rotation = np.radians(degree)

# imgRow = len(sample)
# imgCol = len(sample[0])

imgRow, imgCol = sample.shape

xp = imgRow // 2
yp = imgCol // 2

# newImage = ndimage.rotate(sample, degree, reshape=False)
newRow = round(imgRow * 2)
newColumn = round(imgCol * 2)

xs = round((newRow-imgRow)/2)
ys = round((newColumn-imgCol)/2)

newImage = np.zeros((newRow, newColumn))
# histImage = np.zeros((256))
newImage = newImage.astype(np.uint8)

for x in range(imgRow):
    for y in range(imgCol):

        xn = round(xp + (x - xp) * np.cos(rotation) -
                   (y-yp) * np.sin(rotation))
        yn = round(yp + (x - xp) * np.sin(rotation) +
                   (y-yp) * np.cos(rotation))

        xn += xs
        yn += ys

        newImage[xn, yn] = sample[x, y]
        # print(newImage[xs, ys])

        # histImage[pixel] += 1 / (imgRow * imgCol)

# print()
# print(newImage[:, :])
# cv.imshow('sample', sample)
cv.imshow('result', newImage)
# plt.xlabel("Value")
# plt.ylabel("Probability")
# plt.plot(histImage, color = (0.5, 0.5, 0.5))
# plt.show()
cv.waitKey(0)
