import cv2
import numpy as np
from user_path_input import user_path_input
# function w/ no purpose
def nonFunction(value):
    pass
# convolution kernels
identity_kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
gaussian_kernelOne = cv2.getGaussianKernel(3,0)
gaussian_kernelTwo = cv2.getGaussianKernel(5,0)
box_kernel = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9.0
kernels = [identity_kernel,sharpen_kernel,gaussian_kernelOne,gaussian_kernelTwo,box_kernel]
# function to determine user input and status of application
def current_status():
    # count used to save the images
    count = 1
    while True:
        grayscale = cv2.getTrackbarPos('grayscale','editor page')
        contrast = cv2.getTrackbarPos('contrast','editor page')
        brightness = cv2.getTrackbarPos('brightness','editor page')
        kernel = cv2.getTrackbarPos('filter','editor page')
        # modified images
        color_modified = cv2.filter2D(orig_image,-1,kernels[kernel])
        gray_modified = cv2.filter2D(grayscale_image,-1,kernels[kernel])
        color_modified = cv2.addWeighted(color_modified,contrast, np.zeros_like(orig_image),0,brightness - 50)
        gray_modified = cv2.addWeighted(gray_modified,contrast,np.zeros_like(grayscale_image),0,brightness-50)
        # key_wait usr input, duration of a 100ms this is a integer value
        key_wait = cv2.waitKey(100)
        # to compare we need to change char to int using ord()
        if key_wait == ord('q'):
            break
        elif key_wait == ord('s'):
            # to save image based on user input
            if grayscale == 0:
                cv2.imwrite('edited-{}.png'.format(count),color_modified)
            else:
                cv2.imwrite('edited-{}.png'.format(count),gray_modified)
            count += 1

        # determine the current status on the grayscale bar
        if grayscale == 0:
            cv2.imshow('editor page',color_modified)
        else:
            cv2.imshow('editor page', gray_modified)

# read an image within the same folder and load
orig_image = cv2.imread('rimuru_shizue.jpg')
grayscale_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
# create the screen from the application
cv2.namedWindow('editor page')
# create the necessary trackbars that will handle the functionality of the editor
cv2.createTrackbar('contrast','editor page',1,100,nonFunction)
cv2.createTrackbar('brightness','editor page',50,100,nonFunction)
cv2.createTrackbar('filter','editor page',0,len(kernels)-1, nonFunction)
cv2.createTrackbar('grayscale','editor page',0,1,nonFunction)
# userInput = user_path_input()
# userInput.find_file()
current_status()
# destroyAllWindows after key press
cv2.destroyAllWindows()
