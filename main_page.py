import cv2
import numpy as np

# function w/ no purpose
def nonFunction(value):
    pass

# function to determine user input and status of application
def current_status():
    while True:
        # key_wait usr input, duration of a 100ms this is a integer value
        key_wait = cv2.waitKey(100)
        # to compare we need to change char to int using ord()
        if key_wait == ord('q'):
            break
        elif key_wait == ord('s'):
            # to save image based on user input
            print('Saving option coming soon!!')
            pass
# create the screen from the application
cv2.namedWindow('editor page')
# create the necessary trackbars that will handle the functionality of the editor
cv2.createTrackbar('contrast','editor page',1,100,nonFunction)
cv2.createTrackbar('brightness','editor page',50,100,nonFunction)
cv2.createTrackbar('filter','editor page',0,1,nonFunction)
cv2.createTrackbar('grayscale','editor page',0,1,nonFunction)

current_status()
# destroyAllWindows after key press
cv2.destroyAllWindows()
