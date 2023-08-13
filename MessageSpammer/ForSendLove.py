# Importing necessary packages
import pyautogui as pg 
import time

# Timer
time.sleep(10)

# Initialization of i
i = 0
# Message that wants to be sent
a = "I love you <3"

# While loop for number of messages to send
while i < 10:
    i=i+1
    pg.write(a)
    pg.press("Enter")
