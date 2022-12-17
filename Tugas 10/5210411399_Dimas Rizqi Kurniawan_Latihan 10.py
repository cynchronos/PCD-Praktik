import cv2 as cv
import numpy as np
import os
import numpy as np

img = cv.imread('Tugas 10/Latihan - pekan 10.jpg')

img = cv.resize(img, (500, 700))

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

def ImageModManual(img, degree, scalar, kernel):
    sample = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    rotation = degree * np.pi/180

    imgRow = len(sample)
    imgCol = len(sample[0])


    xp = round(imgRow / 2)
    yp = round(imgCol / 2)

    # Rotasi Citra
    rotation_image = np.zeros((imgRow, imgCol))
    rotation_image = rotation_image.astype(np.uint8)

    for new_row in range(imgRow):
        for new_col in range(imgCol):

            row = round(xp + (new_row - xp) * np.cos(rotation) - (new_col - yp) * np.sin(rotation))
            col = round(yp + (new_row - xp) * np.sin(rotation) + (new_col - yp) * np.cos(rotation))

            if 0 <= row < imgRow and 0 <= col < imgCol:
                rotation_image[new_row, new_col] = sample[row, col]

    # Peningkatan Brightness
    brightness_image = np.zeros((imgRow, imgCol))
    brightness_image = brightness_image.astype(np.uint8)

    for new_row in range(imgRow):
        for new_col in range(imgCol):

            pixel = rotation_image[new_row, new_col] + scalar
            
            if pixel > 255 :
                brightness_image[new_row, new_col] = 255
            else:
                brightness_image[new_row, new_col] = pixel

    # Konvolusi
    convolutional_image = np.zeros((imgRow, imgCol))
    convolutional_image = convolutional_image.astype(np.uint8)

    for convRow in range (1, imgRow-1):
        for convCol in range (1, imgCol-1):
            a = brightness_image[convRow-1,convCol-1] * kernel[0,0]
            b = brightness_image[convRow-1,convCol] * kernel[0,1]
            c = brightness_image[convRow-1,convCol+1] * kernel[0,2]
            d = brightness_image[convRow,convCol-1] * kernel[1,0]
            e = brightness_image[convRow,convCol] * kernel[1,1] 
            f = brightness_image[convRow,convCol+1] * kernel[1,2] 
            g = brightness_image[convRow+1,convCol-1] * kernel[2,0]
            h = brightness_image[convRow+1,convCol] * kernel[2,1]
            i = brightness_image[convRow+1,convCol+1] * kernel[2,2]

            kernel_sum = np.sum(kernel)
            if kernel_sum == 0 :
                kernel_sum = 0
            
            conv_result = np.round((a + b + c + d + e + f + g + h + i) / kernel_sum)

            if conv_result < 0 :
                conv_result = 0
            
            if conv_result > 255 :
                conv_result = 255
            
            convolutional_image[convRow, convCol] = conv_result
    
    cv.imshow('image', sample)
    cv.imshow('rotation', rotation_image)
    cv.imshow('brightness', brightness_image)
    cv.imshow('convolution', convolutional_image)

def ImageModOpenCV(img, degree, scalar, kernel):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Rotasi gambar 5 derajat
    imgRotation = cv.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), degree, 1)
    newImageRotation = cv.warpAffine(img, imgRotation, (img.shape[1], img.shape[0]))

    # Meningkatkan Brightness
    img_increase_brightness = cv.add(newImageRotation, scalar)

    #Konvolusi
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    img_convolution = cv.filter2D(img_increase_brightness, -1, kernel)


    cv.imshow("Image", img)
    cv.imshow("Rotate Image", newImageRotation)
    cv.imshow("Brightness Image", img_increase_brightness)
    cv.imshow("Convolution Image", img_convolution)

# ImageModManual(img=img, degree=-5, scalar=50, kernel=kernel)
ImageModOpenCV(img=img, degree=5, scalar=50, kernel=kernel)
cv.waitKey(0)
