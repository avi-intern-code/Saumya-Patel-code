import cv2
import numpy as np
img = cv2.imread("D:/Internship/Anemoi_Technologies/Training/Images/lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    #cv2.imshow(str(i), layer)

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
# Gaussian pyramids use cv.pyrDown() and cv.pyrUp() functions.

# on some occasions, we need to work with (the same) images in different resolution
# In that case, we will need to create a set of the same image with different resolutions and search for object in all of them. These set of images with different resolutions are called Image Pyramids (because when they are kept in a stack with the highest resolution image at the bottom and the lowest resolution image at top, it looks like a pyramid).

# pyrUp() function increases the size to double of its original size
# pyrDown() function decreases the size to half.
# If we keep the original image as a base image and go on applying pyrDown function on it and keep the images in a vertical stack, it will look like a pyramid. The same is true for upscaling the original image by pyrUp function.
# Gaussian pyramid: Used to downsample images
# Laplacian pyramid: Used to reconstruct an upsampled image from an image lower in the pyramid (with less resolution)
