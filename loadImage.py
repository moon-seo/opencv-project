import cv2 as cv

# Load the image
img = cv.imread("cat.jpg") # path to image

# Display the image in a window
cv.imshow("Display window", img) # window name

# Wait for a keystroke in the window
k = cv.waitKey(0)