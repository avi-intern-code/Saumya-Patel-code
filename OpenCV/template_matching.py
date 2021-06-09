import cv2
import numpy as np
img = cv2.imread("D:/Internship/Anemoi_Technologies/Training/Images/messi5.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("D:/Internship/Anemoi_Technologies/Training/Images/messi_face.JPG", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
# The input image that contains the object we want to detect
# The template of the object (i.e., what we want to detect in the image)
# The template matching method

print(res)
threshold = 0.99;
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose.
#  Template matching is a technique for finding areas of an image that match (are similar) to a template image (patch).
# While the patch must be a rectangle it may be that not all of the rectangle is relevant. In such a case, a mask can be used to isolate the portion of the patch that should be used to find the match.