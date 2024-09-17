import cv2 as cv
import numpy as np

img1 = cv.imread("resources/window.png")
img2 = cv.imread("resources/window2.png")
# You should check if their sizes are the same (skipped here)

# Compute the absolute difference
diff = cv.absdiff(img1, img2)

# Consider pixels with differences as foreground
foreground_mask = np.any(diff > 0, axis = 2).astype(np.uint8) * 255
# np.any(): Check if any element in the array satisfies the given condition
# diff > 0: Check if the values of each pixel in all channels(R, G, B) are greater than 0
# axis = 2: Apply the operation to the third dimension(color channels) of the array
# * 255: Values in the array after astype() are either 0 or 1 -> multiply by 255 to distinguish foreground(1) from background(0) 

cv.imshow("Difference", diff)
cv.imshow("Foreground Mask", foreground_mask)
cv.imshow("Window 1", img1)
cv.imshow("Window 2", img2)

cv.waitKey(0)
cv.destroyAllWindows()