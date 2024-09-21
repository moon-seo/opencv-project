import cv2 as cv
import time
import datetime
import threading

# Function to save frames (for asynchronous processing)
def save_frame(frame, filename):
    cv.imwrite(filename, frame)  # Save the current frame as an image file

capture = cv.VideoCapture(0)   

savetime = time.time()  # Set the initial save time to the current time

while True:
    ret, frame = capture.read()

    if cv.waitKey(10) >= 0: 
        break

    if ret:
        cv.imshow("Camera", frame)

        current = time.time()

        if current - savetime >= 1.0:   # Save frames every second
            frame_filename = datetime.datetime.now().strftime("frame_%Y%m%d_%H%M%S.png")
            threading.Thread(target=save_frame, args=(frame, frame_filename)).start() 
            # Saving frames takes time and can cause keyboard input to be ignored
            # -> Handle it asynchronously in a separate thread to decrease blocking of the UI thread

            savetime = current

capture.release()
cv.destroyAllWindows()