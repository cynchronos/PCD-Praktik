import cv2 as cv

sample = cv.imread('./sample.jpg')
img = cv.resize(sample, (852, 480), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

treshold = 150

th, binary = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)

print(binary)
cv.imshow('sample', binary)

cv.waitKey(0)
cv.destroyAllWindows()