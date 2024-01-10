
import time
import pyautogui

while True:
    pyautogui.mouseDown(677, 336, button='left')
    time.sleep(0.5)
    pyautogui.mouseUp(677, 336, button='left')
    time.sleep(3)
    pyautogui.keyDown("3")
    time.sleep(.25)
    pyautogui.keyUp("3")
    time.sleep(213)