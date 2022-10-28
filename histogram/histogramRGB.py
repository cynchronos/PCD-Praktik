from turtle import color
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

sample = cv.imread('./sample.jpg')

img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

# pecah 3 channel
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# buat row dan kolom
img_row = len(img)
img_col = len(img[0])

# buat matrix baru untuk 3 channel
b_plot = np.zeros((256))
g_plot = np.zeros((256))
r_plot = np.zeros((256))

def rHist(r,g, b, r_plot, g_plot, b_plot):
    # telusuri channel
    for row in range(img_row):
        for col in range(img_col):
            # Ketahui isi pixel 3 channel terlebih dahulu
            pixelr = r[row, col] 
            pixelg = g[row, col]
            pixelb = b[row, col]
            
            # update tiap nilai pixel yang sama dengan index dan tambahkan 1 (if nilai pixel = 2 == index 2 : nilai index2 + 1)
            r_plot[pixelr] += 1  / (img_row * img_col)
            g_plot[pixelg] += 1 / (img_row * img_col)
            b_plot[pixelb] += 1 / (img_row * img_col)

    plt.xlabel("Value")
    plt.ylabel("Probability")
    cv.imshow("img", img)
    plt.plot(b_plot, color = (0,0,1))
    plt.plot(g_plot, color = (0,1,0))
    plt.plot(r_plot, color = (1,0,0))
    plt.show()
    cv.waitKey(0)
rHist(r, g, b, r_plot, g_plot ,b_plot)