import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

sample = cv.imread('./sample.jpg')
img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)

row_len = len(img)
col_len = len(img[0])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

treshold = 157

binary = gray

# manual
# for row in range(row_len):
#     for col in range(col_len):
#         pixel = gray[row, col]
#         if pixel > treshold:
#             binary[row, col] = 255
#         else:
#             binary[row, col] = 0

# opencv
th, binary = cv.threshold(gray, treshold, 255,cv.THRESH_BINARY)

#! Create Histogram GS
# Create 256 row using zeros
bin_plot = np.zeros((256))

# know pixel and add pixel to plot
for binRow in range(row_len):
    for binCol in range(col_len):
        pixel = binary[binRow, binCol]
        
        bin_plot[pixel] += 1 / (row_len * col_len)

# show histogram
plt.xlabel("Value")
plt.ylabel("Probability")
cv.imshow('sample', binary)
plt.plot(bin_plot, color = (0.5, 0.5, 0.5))
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()