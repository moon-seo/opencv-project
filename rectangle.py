import cv2 as cv

# Initialize variables
start_point = None
end_point = None
drawing = False
color = (255, 0, 255) # Set the color

# Callback function that gets called when a mouse event occurs
# 'event' is the mouse event(click, move, etc.), 'x' and 'y' are the current coordinates of the mouse cursor
def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing

    if event == cv.EVENT_LBUTTONDOWN: # When the left mouse button is pressed, start drawing
        drawing = True
        start_point = (x, y)

    elif event == cv.EVENT_MOUSEMOVE:  # When the mouse is moved
        if drawing:
            end_point = (x, y)
    
    elif event == cv.EVENT_LBUTTONUP:  # When the left mouse button is released
        drawing = False
        end_point = (x, y)

        # Draw a rectangle
        cv.rectangle(img, start_point, end_point, color, 2)
        # Display the updated image whenever a mouse event occurs (real-time image update)
        cv.imshow("Image", img) 

img = cv.imread("resources/landscape.jpg")
 
# Create a new window named "Image"
cv.namedWindow("Image")
# Set the callback function to handle mouse events that occur on the specific window
# Mouse events in the "Image" window will be passed to the draw_rectangle() function
cv.setMouseCallback("Image", draw_rectangle)
# Display the image in the window for the first time
cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()