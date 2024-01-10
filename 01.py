import ctypes
import time
# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
ctypes.windll.user32.SetCursorPos(444, 444)
ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
time.sleep(0.1)
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up


ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
time.sleep(0.1)
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
time.sleep(0.1)
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
