import cv2 as cv

sample = cv.imread('./sample.jpg')

img = cv.resize(sample, (1280, 720), interpolation=cv.INTER_AREA)
cv.imshow('sample', img)

cv.waitKey(0)
cv.destroyAllWindows()
