import cv2 as cv
from numpy import zeros, uint8
import matplotlib.pyplot as plt
import os

os.chdir('Responsi 1/')

#! Membaca Citra
cvImg = cv.imread('sample.jpg')

#! Pemisah channel citra
imgBlue = cvImg[:, :, 0]
imgGreen = cvImg[:, :, 1]
imgRed = cvImg[:, :, 2]

# imgBlue,imgGreen,imgRed = cv.split(cvImg)

#! Baris dan kolom citra
imgRow = len(cvImg)
imgColumn = len(cvImg[0])

#! Matrix dan histogram kosong

# Citra
imgGray = zeros((imgRow, imgColumn)).astype(uint8)
imgBrightness = zeros((imgRow, imgColumn)).astype(uint8)
imgBinary = imgBrightness.copy()

# Histogram
histogramBlue = zeros(256)
histogramGreen = zeros(256)
histogramRed = zeros(256)

#! Histogram Citra
def image_histogram(b, g, r):
    for row in range(imgRow):
        for col in range(imgColumn):
            pixelBlue = b[row, col]
            pixelGreen = g[row, col]
            pixelRed = r[row, col]

            histogramBlue[pixelBlue] += 1 / (imgRow * imgColumn)
            histogramGreen[pixelGreen] += 1 / (imgRow * imgColumn)
            histogramRed[pixelRed] += 1 / (imgRow * imgColumn)


#! Convert Ke Citra Grayscale
def convert_to_grayscale(b, g, r) :
    for row in range(imgRow):
        for col in range(imgColumn):
            imgGray[row, col] = round(0.299 * r[row, col] + 0.587 * g[row, col] + 0.114 * b[row, col])
            
    

#! Peningkatan brightness pada citra
def increase_brightness_grayscale_image(image, scalar):
    global imgBrightness
    
    for row in range(imgRow):
        for col in range(imgColumn):
            pixel = image[row, col] + scalar
            
            if pixel > 255 :
                imgBrightness[row, col] = 255
            else:
                imgBrightness[row, col] = pixel
    
    #! OpenCV
    # imgBrightness = cv.add(image, scalar)


#! Konversi citra grayscale ke black and white(binary)
def convert_grayscale_to_binary(image, threshold):
    global imgBinary
    
    for row in range(imgRow):
        for col in range(imgColumn):
            pixel = image[row, col]
            
            if pixel > threshold:
                imgBinary[row, col] = 255
            else:
                imgBinary[row, col] = 0
    
    #! OpenCV
    # th, imgBinary = cv.threshold(image, threshold, 255, cv.THRESH_BINARY)
  
    
#! Proses
image_histogram(imgBlue, imgGreen, imgRed)
convert_to_grayscale(imgBlue, imgGreen, imgRed)

scalar = 30
increase_brightness_grayscale_image(imgGray, scalar)

threshold = 160
convert_grayscale_to_binary(imgBrightness, threshold)

#! Hasil

# Citra
cv.imshow('image', cvImg)
cv.imshow('Image Grayscale', imgGray)
cv.imshow('Image Brightness', imgBrightness)
cv.imshow('Image Black & White', imgBinary)

# Histogram
plt.figure(figsize=(13,5))

plt.subplots_adjust(wspace=0.4)
plt.subplot(1,3,1)
plt.plot(histogramBlue, color=(0, 0, 1))
plt.title('Blue Histogram')
plt.xlabel("Nilai Citra")
plt.ylabel("Probabilitas Kemunculan Citra")

plt.subplot(1,3,2)
plt.plot(histogramGreen, color=(0, 1, 0))
plt.title('Green Histogram')
plt.xlabel("Nilai Citra")
plt.ylabel("Probabilitas Kemunculan Citra")

plt.subplot(1,3,3)
plt.plot(histogramRed, color=(1, 0, 0))
plt.title('Red Histogram')
plt.xlabel("Nilai Citra")
plt.ylabel("Probabilitas Kemunculan Citra")

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
