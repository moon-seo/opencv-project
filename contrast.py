import cv2 as cv
import numpy as np

# Load the image in grayscale
img = cv.imread("resources/cat.jpg", cv.IMREAD_GRAYSCALE)

alpha = 0.5 # Contrast control (0 means no change)

# Adjust pixel values in the grayscale image to control contrast
contrasted = np.clip((1 + alpha) * img - 128 * alpha, 0, 255).astype(np.uint8)
# (1 + alpha) * img: Adjust brightness with alpha (multiplies all pixel values to control contrast)
# - 128 * alpha: Shift all pixel values to control contrast based on the mid tone (128 is the midpoint of a typical grayscale image -> this shifts pixel values linearlly for contrast adjustment)
# np.clip(..., 0, 255): Limit the result value between 0-255 (saturated arithmetic)
# .astype(np.uint8): convert the data to an 8 bit unsigned integer (<- image pixel values must be between 0-255)

cv.imshow("Original Image", img)
cv.imshow("Contrasted Image", contrasted)

cv.waitKey(0)
cv.destroyAllWindows()