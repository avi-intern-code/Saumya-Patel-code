import cv2

img = cv2.imread('D:/Internship/Anemoi_Technologies/Training/Images/lena.jpg', -1)
cv2.imshow('D:/Internship/Anemoi_Technologies/Training/Images/image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('D:/Internship/Anemoi_Technologies/Training/Images/lena_copy.png', img)
  cv2.destroyAllWindows()

# cv2.imread() Second argument is a flag which specifies the way image should be read.
# flag integer value description
# cv2.IMREAD_COLOR 1 Loads a color image.
# cv2.IMREAD_GRAYSCALE 0 Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED -1 Loads image as such including alpha channel