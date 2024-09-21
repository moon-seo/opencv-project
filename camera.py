# If you're a mac and iphone user, you can use your iphone as the default camera(id: 0)
# This is a macOS feature called Continuity Camera which is automatically set

import cv2 as cv

capture = cv.VideoCapture(0)    # Open the camera
# The parameter(index in this func) is the ID of the camera device
# 0 refers to the default camera of your system (usually the built-in one)

while True:
    ret, frame = capture.read()
    # ret(return) is a boolean value indicating if frames are successfully read
    # frame contains the image data of the read frame
    cv.imshow("Camera", frame)

    if cv.waitKey(1) >= 0:  # Exit when any key pressed
        break

capture.release()
cv.destroyAllWindows()