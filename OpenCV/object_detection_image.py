import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

# createTrackbar( TrackbarName, "Linear Blend", &alpha_slider, alpha_slider_max, on_trackbar );
# Our Trackbar has a label TrackbarName
# The Trackbar is located in the window named Linear Blend
# The Trackbar values will be in the range from 0 to alpha_slider_max (the minimum limit is always zero).
# The numerical value of Trackbar is stored in alpha_slider
# Whenever the user moves the Trackbar, the callback function on_trackbar is called

while True:
    frame = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cvtColor() method of cv2 library to convert the color of an image from one color space to another

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # l_b = np.array([110, 50, 50])
    # u_b = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)
    #  hsv is the input image. ‘lowerb’ and ‘upperb’ denotes the lower and upper boundary of the threshold region.

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

# we will be Implementing color and shape-based object detection and tracking using  hue-saturation-value (HSV) color model.
# For Choosing the correct upper and lower HSV boundaries for color detection with`cv::inRange` (OpenCV) we will use trackbar.
