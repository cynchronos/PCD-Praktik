import cv2 as cv
import numpy as np
import os
from scipy import ndimage

# os.chdir("/mnt/01D8CC470068EB90/Github/PCD-Praktik/Geometri/")
# img = cv.imread('a.jpg')

# img = cv.resize(img, (5, 7))

# sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sample = [
    [135, 163, 164, 164, 164],
    [159, 104, 106, 106, 126],
    [178, 183, 169, 169, 154],
    [192, 193, 178, 178, 116],
    [199, 132, 135, 135, 155],
    [192, 193, 178, 178, 116],
    [199, 132, 135, 135, 155]
]

sample = np.array(sample)

degree = -20

rotation = degree * (np.pi/180)

imgRow = len(sample)
imgCol = len(sample[0])

xp = imgRow // 2
yp = imgCol // 2

newRow = round(imgRow * 2)
newColumn = round(imgCol * 2)

xs = round((newRow-imgRow)/2)
ys = round((newColumn-imgCol)/2)

newImage = np.zeros((newRow, newColumn))
newImage = newImage.astype(np.uint8)

# arrayott = ndimage.rotate(sample, degree, reshape=False)

for x in range(imgRow):
    for y in range(imgCol):
        print("(", x, ",", y, ")\t x' = ", xp, "+ (", x, "-", xp,
              ") * cos(-20°) - (", y, "-", yp, ") * sin(-20°)")
        xn = round(xp + (x - xp) * np.cos(rotation) -
                   (y-yp) * np.sin(rotation))
        print("\t\tx' = ", xn," + ", xs)
        newxn = xn + xs
        print("\t\tx'= ", newxn)
        print()
        print("\t\ty' = ", yp, "+ (", x, "-", xp,
              ") * sin(-20°) + (", y, "-", yp, ") * cos(-20°)")
        yn = round(yp + (x - xp) * np.sin(rotation) +
                   (y-yp) * np.cos(rotation))
        print("\t\ty' = ", yn," + ", ys)
        newyn = yn + ys
        print("\t\ty = ", newyn)
        print()
        print("\t\t(x', y') = ", "(", newxn,",", newyn, ")")
        print("\n")

        newImage[xn + xs, yn + ys] = sample[x, y]


print(newImage[:, :])
# print(ys)
# cv.imshow('sample', sample)
# cv.imshow('result', newImage)
# cv.waitKey(0)
