import cv2 as cv
import numpy as np
import os

os.chdir("/mnt/01D8CC470068EB90/Github/PCD-Praktik/Geometri/")
img = cv.imread('a.jpg')

img = cv.resize(img, (5, 7))

sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

degree = -20

rotation = degree * (np.pi/180)

imgRow = len(sample)
imgCol = len(sample[0])

xp = imgRow // 2
yp = imgCol // 2

newImage = np.zeros((imgRow, imgCol))
newImage = newImage.astype(np.uint8)

for x in range(imgRow):
    for y in range(imgCol):
        print("(",x,",", y, ")\t x' = ", xp, "+ (",x, "-", xp,") * cos(-20°) - (",y,"-",yp,") * sin(-20°)")
        xn = round(xp + (x - xp) * np.cos(rotation) - (y-yp) * np.sin(rotation))
        print("\t\tx'= ", xn)
        print()
        print("\t\ty' = ", yp, "+ (",x, "-", xp,") * sin(-20°) - (",y,"-",yp,") * cos(-20°)")
        yn = round(yp + (x - xp) * np.sin(rotation) + (y-yp) * np.cos(rotation))
        print("\t\ty = ", yn)
        print()
        print("\t\t(x', y') = ", "(",xn,",",yn,")")
        print("\n")

        # if 0 <= xn < imgRow and 0 <= yn < imgCol:
        #     newImage[x, y] = sample[xn, yn]



# print(xn)
# print(rotation)
# cv.imshow('sample', sample)
# cv.imshow('result', newImage)
# cv.waitKey(0)