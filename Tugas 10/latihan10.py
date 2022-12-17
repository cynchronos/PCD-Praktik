import cv2 as cv
import numpy as np
import os

img = cv.imread('Tugas 10/Latihan - pekan 10.jpg')

img = cv.resize(img, (500, 700))

def ManualRotation(img, degree):
    sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    rotation = degree * np.pi/180

    # rotation = np.radians(degree)

    imgRow = len(sample)
    imgCol = len(sample[0])

    # imgRow, imgCol = sample.shape

    xp = round(imgRow / 2)
    yp = round(imgCol / 2)

    newImage = np.zeros((imgRow, imgCol))
    newImage = newImage.astype(np.uint8)

    for new_row in range(imgRow):
        for new_col in range(imgCol):

            row = round(xp + (new_row - xp) * np.cos(rotation) - (new_col - yp) * np.sin(rotation))
            col = round(yp + (new_row - xp) * np.sin(rotation) + (new_col - yp) * np.cos(rotation))

            if 0 <= row < imgRow and 0 <= col < imgCol:
                newImage[new_row, new_col] = sample[row, col]

    # newImage.reverse()
    cv.imshow('resultManual', newImage)

ManualRotation(img=img, degree=-5)
cv.waitKey(0)
