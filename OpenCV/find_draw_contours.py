import numpy as np
import cv2

img = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # returns a modified image as the first of three return parameters.\
#  first one is source image
# second is contour retrieval mode,
# third is contour approximation method

# outputs a modified image, the contours and hierarchy.
# contours is a Python list of all the contours in the image
# Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.

print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3) # It can also be used to draw any shape provided you have its boundary points.
# first argument is source image
# second argument is the contours which should be passed as a Python list
# third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.findContours(), cv2.drawContours().
# The function retrieves contours from the binary image.
# The contours are a useful tool for shape analysis and object detection and recognition.

# Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.