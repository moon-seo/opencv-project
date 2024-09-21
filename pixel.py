# Draw a rectangle by adjusting pixel values one by one (w/o any functions)
# to practice modifying each pixel value

import cv2 as cv
import numpy as np

img = cv.imread("resources/cat.jpg")

# Coordinates of the rectangle
top_left = (140, 110)
bottom_right = (330, 290)

color = (0, 255, 0)

for i in range(top_left[1], bottom_right[1]):
    img[i, top_left[0]] = color    # Left border
    img[i, bottom_right[0]-1] = color  # Right border

for j in range(top_left[0], bottom_right[0]):
    img[top_left[1], j] = color    # Top border
    img[bottom_right[1]-1, j] = color  # Bottom border

cv.imshow("Drawing a rectangle by adjusting pixel values", img)

cv.waitKey(0)
cv.destroyAllWindows()