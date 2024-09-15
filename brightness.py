import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")

# Increase brightness (add 50 to all pixel values)
brightened = cv.add(img, (50, 50, 50))

# Decrease brightness (subtract 50 from all pixel values)
darkened = cv.subtract(img, (50, 50, 50))

# Pixel values must be between 0 and 255, so Saturation Arithmetic is used to limit the calcultation results within this range.
# (If a pixel value excceds 255, it is set to 255; if if falls below 0, it is set to 0.)
# But when you use cv.add() and cv.subtract(), they automatically handle saturated arithmetic. 
# (not needing additional checks for overflow or underflow)

cv.imshow("Bright Image", brightened)
cv.imshow("Dark Image", darkened)
cv.imshow("Original Image", img)

cv.waitKey(0)