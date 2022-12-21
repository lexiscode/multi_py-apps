# Installed PyAutoGUI and Pillow packages 

# https://pyautogui.readthedocs.io/en/latest/quickstart.html
# https://www.geeksforgeeks.org/python-time-module/
# https://www.geeksforgeeks.org/python-gui-tkinter/

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
    # we also created a new sub-folder to store all screenshots using its abolute path
    name = f"C:/Users/nwoko/PycharmProjects/myfirstproject/screenshots/{name}.png"
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

    
    
###USING PYTHON GUI - TKINTER###

#import time
import pyautogui
import random
import tkinter as tk

def screenshot():
    # name = int(round(time.time() * 1000))
    name = random.randint(1, 101)
    name = f"C:/Users/nwoko/PycharmProjects/myfirstproject/screenshots/{name}.png"
    # time.sleep(5), we can use our GUI to make it run ASAP whenever we click the button
    img = pyautogui.screenshot(name)
    img.show()

# screenshot(), we don't need to call the function here, since its already called in our GUI below

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creating buttons inside the frame, its label and its action/command which is the screenshot()
# screenshot action button
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)
# close screenshot app button
close = tk.Button(
    frame,
    text="Quit",
    command=quit
)
close.pack(side=tk.LEFT)

# runs the GUI
root.mainloop()
