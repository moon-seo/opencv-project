import cv2 as cv

# Images should have the same size and the same number of channels.
img1 = cv.imread("dog.jpg")
img2 = cv.imread("dog2.jpg")
img3 = cv.imread("vignette.jpg")

# Add the two images
added = cv.add(img1, img2)

# Subtract the images
subtracted = cv.subtract(img2, img3)

cv.imshow("Added Image", added)
cv.imshow("Subtracted Image", subtracted)

cv.waitKey(0)