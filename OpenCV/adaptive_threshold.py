import cv2 as cv
import numpy as np

img = cv.imread('D:/Internship/Anemoi_Technologies/Training/Images/sudoku.png',0)

# adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# src − An object of the class Mat representing the source (input) image.
# dst − An object of the class Mat representing the destination (output) image.
# maxValue − A variable of double type representing the value that is to be given if pixel value is more than the threshold value.
# adaptiveMethod − A variable of integer the type representing the adaptive method to be used. This will be either of the following two values
# thresholdType − A variable of integer type representing the type of threshold to be used.
# blockSize − A variable of the integer type representing size of the pixelneighborhood used to calculate the threshold value.
# C − A variable of double type representing the constant used in the both methods (subtracted from the mean or weighted mean).

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) # The threshold value is the mean of the neighbourhood area minus the constant C
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) # The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()

# Adaptive Thresholding algorithm provide the image in which Threshold values vary over the image as a  function of  local image characteristics.
# So Adaptive Thresholding involves two following steps
# (i) Divide image into strips
# (ii) Apply global threshold method to each strip.

# So in Adaptive Thresholding, Threshold depends on both f(x,y) and p(x,y). Adaptive thresholding changes the threshold dynamically over the image.
# Adaptive thresholding typically takes a gray scale or color image as input and, in the simplest implementation, outputs a binary image representing the segmentation.

# daptive thresholding is the method where the threshold value is calculated for smaller regions and therefore, there will be different threshold values for different regions.
# if an image has different lighting conditions in different areas. In that case, adaptive thresholding can help.
# the algorithm determines the threshold for a pixel based on a small region around it.
# we get different thresholds for different regions of the same image which gives better results for images with varying illumination.
