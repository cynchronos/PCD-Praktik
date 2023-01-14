import cv2 as cv
import numpy as np
import os

os.chdir('Responsi 2/')

image = cv.imread('Bunga_Mawar_Merah.jpg')
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

img_scale = image.copy()
img_sharp = image.copy()
img_adjust = image.copy()

def image_zoom(img, scale):
    global img_scale
    scaling_row = round(image.shape[0] * scale)
    scaling_col = round(image.shape[1] * scale)

    imgScale = np.zeros((scaling_row, scaling_col, 3))
    imgScale = imgScale.astype(np.uint8)

    for newRow in range(scaling_row):
        for newCol in range(scaling_col):
            row = int(newRow / scale)
            col = int(newCol / scale)

            imgScale[newRow, newCol] = img[row, col]
    
    img_scale = imgScale.copy()

def image_sharpening(img, kernel):
    global image_sharpening

    row_size = img.shape[0]
    col_size = img.shape[1]
    channel = img.shape[2]
   
    zero_padding = np.zeros((row_size + 2, col_size + 2, channel))

    conv_image = np.zeros((row_size, col_size, channel))

    # memasukkan citra awal ke matriks_baru
    for row in range(row_size):
        for col in range(col_size):
                zero_padding[row + 1, col + 1] = img[row, col]


    #loop mulai dari pixel (1,1,0)
    for row in range(1,row_size-1):
        for col in range(1,col_size-1):
            for ch in range (channel):
                #baca dan kalikan matriks 3x3 dari gambar awal dengan kernel 3x3
                a = zero_padding[row-1,col-1,ch] * kernel[0,0]   #kiri atas (Baris sebelum titik tengah dan kolom sebelum titik tengah)
                b = zero_padding[row-1,col,ch] * kernel[0,1]     #tengah atas (Baris sebelum titik tengah dan kolom sama dengan titik tengah)
                c = zero_padding[row-1,col+1,ch] * kernel[0,2]   #kanan atas
                d = zero_padding[row,col-1,ch] * kernel[1,0]     #kiri
                e = zero_padding[row,col,ch] * kernel[1,1]       #tengah matriks
                f = zero_padding[row,col+1,ch] * kernel[1,2]     #kanan
                g = zero_padding[row+1,col-1,ch] * kernel[2,0]   #kiri bawah
                h = zero_padding[row+1,col,ch] * kernel[2,1]     #tengah bawah
                i = zero_padding[row+1,col+1,ch] * kernel[2,2]   #kanan bawah

                #hitung total nilai dalam kernel
                sum_kernel = np.sum(kernel)
                if (sum_kernel == 0):
                    sum_kernel = 1

                #hitung hasil konvolusi
                convolution = np.round((a + b + c + d + e + f + g + h + i) / sum_kernel)

                #perbaiki hasil konvolusi jika di luar rentang 0-255
                if (convolution < 0):
                    convolution = 0
                
                if (convolution > 255):
                    convolution = 255

                #isikan hasil konvolusi ke matriks_baru
                conv_image[row, col, ch] = convolution

    #konversi citra_translasi menjadi uint8
    conv_image = conv_image.astype(np.uint8)
    image_sharpening = conv_image.copy()

def image_recolor(img, red_adjust, green_adjust, blue_adjust):
    global img_adjust

    row_size = img.shape[0]
    col_size = img.shape[1]

    image_adjust = np.zeros((row_size, col_size, 3))

    for row in range(row_size):
        for col in range(col_size):
            for ch in range(3):
                if ch == 0 :
                    pixel = img[row, col, ch] + blue_adjust
                elif ch == 1:
                    pixel  = img[row, col, ch] + green_adjust
                else:
                    pixel = img[row, col, ch] + red_adjust
            
                if pixel > 255 :
                    pixel = 255
                elif pixel < 0 :
                    pixel = 0
                else:
                    pixel = pixel
                
                image_adjust[row, col, ch] = pixel

    img_adjust = image_adjust.astype(np.uint8).copy()

image_zoom(img=image, scale=1.5)
image_sharpening(img=img_scale, kernel=kernel)
image_recolor(img=image_sharpening, red_adjust= -30, green_adjust=20, blue_adjust=20)
cv.imshow('image', image)
cv.imshow('image_scale', img_scale)
cv.imshow('convolution image', image_sharpening)
cv.imshow('image_adjust', img_adjust)
cv.waitKey(0)
