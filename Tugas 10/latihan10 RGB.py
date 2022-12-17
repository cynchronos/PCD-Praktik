import cv2 as cv
import numpy as np
import os
import numpy as np

img = cv.imread('Tugas 10/Latihan - pekan 10.jpg')

img = cv.resize(img, (500, 700))

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

def ImageMod(img, degree, scalar, kernel):
    sample = img

    rotation = degree * np.pi/180

    scalar = scalar

    imgRow = len(sample)
    imgCol = len(sample[0])
    imgCh = len(sample[0,0])
    # imgRow, imgCol = sample.shape

    xp = round(imgRow / 2)
    yp = round(imgCol / 2)

    newImage = np.zeros((imgRow, imgCol, imgCh))
    newImage = newImage.astype(np.uint8)
    

    for new_row in range(imgRow):
        for new_col in range(imgCol):
            for new_ch in range(imgCh):
                row = round(xp + (new_row - xp) * np.cos(rotation) - (new_col - yp) * np.sin(rotation))
                col = round(yp + (new_row - xp) * np.sin(rotation) + (new_col - yp) * np.cos(rotation))

                if 0 <= row < imgRow and 0 <= col < imgCol:
                    newImage[new_row, new_col, new_ch] = sample[row, col, new_ch]

                pixel = newImage[new_row, new_col, new_ch] + scalar
                
                if pixel > 255 :
                    newImage[new_row, new_col, new_ch] = 255
                else:
                    newImage[new_row, new_col, new_ch] = pixel

    convImage = np.zeros((imgRow, imgCol, imgCh))
    convImage = newImage.astype(np.uint8)

    for convRow in range (1, imgRow-1):
        for convCol in range (1, imgCol-1):
            for convCh in range (imgCh):
                a = newImage[convRow-1,convCol-1] * kernel[0,0]
                b = newImage[convRow-1,convCol] * kernel[0,1]    
                c = newImage[convRow-1,convCol+1] * kernel[0,2] 
                d = newImage[convRow,convCol-1] * kernel[1,0] 
                e = newImage[convRow,convCol] * kernel[1,1]     
                f = newImage[convRow,convCol+1] * kernel[1,2]    
                g = newImage[convRow+1,convCol-1] * kernel[2,0]  
                h = newImage[convRow+1,convCol] * kernel[2,1]
                i = newImage[convRow+1,convCol+1] * kernel[2,2]

            kernel_sum = np.sum(kernel)
            if kernel_sum == 0 :
                kernel_sum = 0
            
            conv_result = np.round((a + b + c + d + e + f + g + h + i) / kernel_sum)

            if conv_result < 0 :
                conv_result = 0
            
            if conv_result > 255 :
                conv_result = 255
            
            convImage[convRow, convCol] = conv_result
    
    cv.imshow('resultManual', convImage)

ImageMod(img=img, degree=-5, scalar=0, kernel=kernel)
cv.waitKey(0)
