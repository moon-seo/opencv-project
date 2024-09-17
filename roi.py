import cv2 as cv

img = cv.imread("resources/landscape.jpg")

# Predefine the starting coordinates(x, y) and width(w), height(h) of the ROI
x, y, w, h = 670, 380, 150, 150
# Extract the region from the image based on the predefined coordinates and store it in ROI
predefined_roi = img[y:y+h, x:x+w]
cv.imshow("Predefined Region of Interest", predefined_roi)

# You can directly select the ROI by dragging with the mouse
x, y, w, h = cv.selectROI("Image", img)
# Check if the width(w) and height(h) of the selected area are greater than 0. (verify if the area is properly selected)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv.imshow("Region of Interest", roi)

cv.waitKey(0)
cv.destroyAllWindows()