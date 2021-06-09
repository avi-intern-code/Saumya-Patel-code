import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/Halftone_Gaussian_Blur.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cvtColor() method of cv2 library to convert the color of an image from one color space to another

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel) # to convolve a kernel with an image
blur = cv2.blur(img, (5, 5)) # This is done by convolving an image with a normalized box filter. It simply takes the average of all the pixels under the kernel area and replaces the central element.
# src: Source image
# dst: Destination image
# Size( w, h ): Defines the size of the kernel to be used ( of width w pixels and height h pixels)
# Point(-1, -1): Indicates where the anchor point (the pixel evaluated) is located with respect to the neighborhood. If there is a negative value, then the center of the kernel is considered the anchor point.

gblur = cv2.GaussianBlur(img, (5, 5), 0) # instead of a box filter, a Gaussian kernel is used.
# src: Source image
# dst: Destination image
# Size(w, h): The size of the kernel to be used (the neighbors to be considered). w and h have to be odd and positive numbers otherwise the size will be calculated using the σx and σy arguments.
# σx: The standard deviation in x. Writing 0 implies that σx is calculated using kernel size.
# σy: The standard deviation in y. Writing 0 implies that σy is calculated using kernel size.

median = cv2.medianBlur(img, 5) # instead of a box filter, a Gaussian kernel is used.
# src: Source image
# dst: Destination image, must be the same type as src
# i: Size of the kernel (only one because we use a square window). Must be odd.

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters.
# src: Source image
# dst: Destination image
# d: The diameter of each pixel neighborhood.
# σColor: Standard deviation in the color space.
# σSpace: Standard deviation in the coordinate space (in pixel terms)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# We will learn different morphological operations like 2 D Convolution(Image Filtering ) and Image Blurring(Image Smoothing) using Averaging, Gaussian Blurring, Median Blurring, Bilateral Filtering etc.We will see different functions like: cv.filter2D(), cv.blur(), cv.GaussianBlur(), cv.medianBlur(), cv.bilateralFilter() etc.

