import cv2 as cv
import numpy as np

img = cv.imread('D:/Internship/Anemoi_Technologies/Training/Images/gradient.png',0)

# The function cv.threshold is used to apply the thresholding
# The first argument is the source image, which should be a grayscale image
# The second argument is the threshold value which is used to classify the pixel values.
# The third argument is the maximum value which is assigned to pixel values exceeding the threshold.
# The fourth parameter is the function of  different types of thresholding.

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # dst(x,y)={maxval if src(x,y)>thresh or 0 otherwise
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) # dst(x,y)={0 if src(x,y)>thresh or maxval otherwise
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # dst(x,y)={threshold if src(x,y)>thresh or src(x,y) otherwise
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # dst(x,y)={src(x,y) if src(x,y)>thresh or 0 otherwise
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # dst(x,y)={0 if src(x,y)>thresh or src(x,y) otherwise

# The first output is the threshold that was used
#  the second output is the thresholded image.

cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()

# In simple thresholding, the threshold value is global, i.e., it is same for all the pixels in the image.
# Simple Image Thresholding is used for image segmentation. Thresholding is the simplest method of image segmentation. From a grayscale image, thresholding can be used to create binary images.
# In Thresholding we Pick a threshold T.
# 1.Pixels above threshold get new intensity A.
# 2.Pixels below threshold get new intensity B.
# In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.
# Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255). Thresholding is a very popular segmentation technique, used for separating an object considered as a foreground from its background. A threshold is a value which has two regions on its either side i.e. below the threshold or above the threshold.
# In Computer Vision, this technique of thresholding is done on grayscale images. So initially, the image has to be converted in grayscale color space.