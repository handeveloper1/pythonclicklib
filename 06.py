import ctypes
import time
import win32api, win32con


def lclick(x,y):
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    time.sleep(0.15)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
    time.sleep(1)


def hover(self, sleep=1.0):
    ctypes.windll.user32.SetCursorPos(self.x, self.y)
    time.sleep(sleep)

lclick(344,444)