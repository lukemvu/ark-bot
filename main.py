
import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui
from PIL import ImageGrab

# Change the working directory to the folde this script is in
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while(True):

    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done.')