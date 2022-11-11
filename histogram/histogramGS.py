from turtle import color
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

sample = cv.imread('./sample.jpg')

img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

# Convert to Grayscale
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# save amount of row and column
row_len = len(img)
col_len = len(img[0])

# Noob Convert/Mathematical
# img_gray = np.zeros((row_len, col_len))
# for row in range(row_len):
#     for col in range(col_len):
#         # worst grayscale
#         # gray[row, col] = round((r[row, col] + g[row, col] + b[row, col]) / 3)
#         # best grayscale
#         img_gray[row, col] = round(0.299 * r[row, col] + 0.587 * g[row, col] + 0.114 * b[row, col])

# # Convert integer from array to unsigned integer for remove bug on matrix image
# img_gray = img_gray.astype(np.uint8)

# Pro Convert
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#! Create Histogram GS

# Create 256 row using zeros
gs_plot = np.zeros((256))

# know pixel and add pixel to plot
for gsRow in range(row_len):
    for gsCol in range(col_len):
        pixel = img_gray[gsRow, gsCol]
        
        gs_plot[pixel] += 1 / (row_len * col_len)

# show histogram
plt.xlabel("Value")
plt.ylabel("Probability")
cv.imshow('sample', img_gray)
plt.plot(gs_plot, color = (0.5, 0.5, 0.5))
plt.show()


# cv.imshow('sample', img)
cv.waitKey(0)
cv.destroyAllWindows()
