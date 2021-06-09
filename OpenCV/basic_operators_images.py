import numpy as mp
import cv2

img = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/messi5.jpg')
img2 = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/opencv-logo.png')

print(img.shape) #returns a tuple of number of rows, columns, and channels
print(img.size) #returns Total number of pixels is accessed
print(img.dtype) #returns Image datatype is obtained
b, g, r = cv2.split(img) #output vector of arrays; the arrays themselves are reallocated, if needed.
# b, g, r = cv2.split(img2) #output vector of arrays; the arrays themselves are reallocated, if needed.
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
img = cv2.merge( (b, g, r)) #The number of channels will be the total number of channels in the matrix array.

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512)) #resize the image
img2 = cv2.resize(img2, (512, 512)) #resize the image

# dst = cv2.add(img, img2); #Calculates the per-element sum of two arrays or an array and a scalar.
dst = cv2.addWeighted(img, .5, img2, .5, 0); #Calculates the weighted sum of two arrays.
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()