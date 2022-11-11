import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir("/mnt/01D8CC470068EB90/Github/PCD-Praktik/Geometri/")
img = cv.imread('a.jpg')

img = cv.resize(img, (500, 700))

sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

degree = 20

# rotation = degree * (np.pi/180)

rotation = np.radians(degree)

# imgRow = len(sample)
# imgCol = len(sample[0])

imgRow, imgCol = sample.shape

xp = imgRow // 2
yp = imgCol // 2

newImage = np.zeros((imgRow, imgCol))
histImage = np.zeros((256))
newImage = newImage.astype(np.uint8)

for x in range(imgRow):
    for y in range(imgCol):
        pixel = sample[x, y]
        
        xn = round(xp + (x - xp) * np.cos(rotation) - (y-yp) * np.sin(rotation))
        yn = round(yp + (x - xp) * np.sin(rotation) + (y-yp) * np.cos(rotation))

        if 0 <= xn < imgRow and 0 <= yn < imgCol:
            newImage[x, y] = sample[xn, yn]
        
        histImage[pixel] += 1 / (imgRow * imgCol)

cv.imshow('sample', sample)
cv.imshow('result', newImage)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.plot(histImage, color = (0.5, 0.5, 0.5))
plt.show()
cv.waitKey(0)