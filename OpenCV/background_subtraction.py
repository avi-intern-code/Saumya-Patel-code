import numpy as np
# import cv2 as cv
cap = cv2.VideoCapture('D:/Internship/Anemoi_Technologies/Training/Images/vtest.avi')

# creating object
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG(); # Gaussian Mixture-based Background/Foreground Segmentation Algorithm
fgbg2 = cv2.createBackgroundSubtractorMOG2(); # t is also a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. It provides better adaptability to varying scenes due illumination changes etc.
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG(); # This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation. This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation.

# Create and update the background model by using cv::BackgroundSubtractor class;

# capture frames from a camera
cap = cv2.VideoCapture(0);
while (1):
    # read frames
    ret, img = cap.read();

    # apply mask for background subtraction
    fgmask1 = fgbg1.apply(img);
    fgmask2 = fgbg2.apply(img);
    fgmask3 = fgbg3.apply(img);

    cv2.imshow('Original', img);
    cv2.imshow('MOG', fgmask1);
    cv2.imshow('MOG2', fgmask2);
    cv2.imshow('GMG', fgmask3);
    k = cv2.waitKey(30) & 0xff;
    if k == 27:
        break;

cap.release()
cv.destroyAllWindows()

# # kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
# # fgbg = cv.bgsegm.BackgroundSubtractorGMG()
# # fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)
# # fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     fgmask = fgbg.apply(frame)
#     # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
#
#     cv.imshow('Frame', frame)
#     cv.imshow('FG MASK Frame', fgmask)
#
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q' or keyboard == 27:
#         break


# Corner detection with Harris Corner Detection method using OpenCV and python is very easy. Shi Tomasi Corner Detector is the modification of Harris Corner Detection.
# Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels belonging to moving objects in the scene) by using static cameras.
# As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene.