import cv2
import numpy as np
from user_path_input import user_path_input
# function w/ no purpose
def nonFunction(value):
    pass
# function to determine user input and status of application
def current_status():
    while True:
        grayscale = cv2.getTrackbarPos('grayscale','editor page')
        # key_wait usr input, duration of a 100ms this is a integer value
        key_wait = cv2.waitKey(100)
        # to compare we need to change char to int using ord()
        if key_wait == ord('q'):
            break
        elif key_wait == ord('s'):
            # to save image based on user input
            print('Saving option coming soon!!')
            pass
        # determine the current status on the grayscale bar
        if grayscale == 0:
            cv2.imshow('editor page',orig_image)
        else:
            cv2.imshow('editor page', grayscale_image)

# read an image within the same folder and load
orig_image = cv2.imread('rimuru_shizue.jpg')
grayscale_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
# create the screen from the application
cv2.namedWindow('editor page')
# create the necessary trackbars that will handle the functionality of the editor
cv2.createTrackbar('contrast','editor page',1,100,nonFunction)
cv2.createTrackbar('brightness','editor page',50,100,nonFunction)
cv2.createTrackbar('filter','editor page',0,1,nonFunction)
cv2.createTrackbar('grayscale','editor page',0,1,nonFunction)
# userInput = user_path_input()
# userInput.find_file()
current_status()
# destroyAllWindows after key press
cv2.destroyAllWindows()
