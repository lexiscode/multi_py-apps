# Installed PyAutoGUI and Pillow also

import time
import pyautogui


def screenshot():
    # this is the waiting seconds before the screenshot() functionn runs
    time.sleep(5)
    # this runs the screenshot() and saves the image as test.png
    img = pyautogui.screenshot('test.png')
    # this displayed the screenshotted image to us on our screen
    img.show()

# calling the function
screenshot()

#The above overwrites previous screenshots that are made each time the program is run
#To avoid this and save each with its own different names, we can modify the function as below

def screenshot():
    # we can replace below using the random.randint() to generate a random number and store it in the 'name' variable
    # that then will also mean we will need to import random module
    name = int(round(time.time() * 1000))
    name = f"{name}.png"
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
