import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)
# We initialize our rectangle image as a 250 x 500 NumPy array on Line 6. We then draw a 250 x 250 white rectangle at the center of the image.

img2 = cv2.imread("D:/Internship/Anemoi_Technologies/Training/Images/image_1.png")

bitAnd = cv2.bitwise_and(img2, img1) # A bitwise AND is true if and only if both pixels are greater than zero.
bitOr = cv2.bitwise_or(img2, img1) # A bitwise OR is true if either of the two pixels is greater than zero.
bitXor = cv2.bitwise_xor(img1, img2) # A bitwise XOR is true if and only if one of the two pixels is greater than zero, but not both.
bitNot1 = cv2.bitwise_not(img1) # A bitwise NOT inverts the “on” and “off” pixels in an image.
bitNot2 = cv2.bitwise_not(img2) # A bitwise NOT inverts the “on” and “off” pixels in an image.

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# This includes bitwise AND, OR, NOT and XOR operations. bitwise_and, bitwise_or, bitwise_xor, bitwise_not) in an image in OpenCV. Bitwise operations likebitwise_and(), bitwise_or(), bitwise_xor(), and bitwise_not() are
#  useful when working with masks