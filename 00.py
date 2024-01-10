# Created by BaiJiFeiLong@gmail.com at 2022/2/10 22:27

from ctypes import WINFUNCTYPE, c_int, Structure, cast, POINTER, windll
from ctypes.wintypes import LPARAM, WPARAM, DWORD, PULONG, LONG

import win32con
import win32gui


def genStruct(name="Structure", **kwargs):
    return type(name, (Structure,), dict(
        _fields_=list(kwargs.items()),
        __str__=lambda self: "%s(%s)" % (name, ",".join("%s=%s" % (k, getattr(self, k)) for k in kwargs))
    ))


@WINFUNCTYPE(LPARAM, c_int, WPARAM, LPARAM)
def hookProc(nCode, wParam, lParam):
    msg = cast(lParam, POINTER(HookStruct))[0]
    print(msgDict[wParam], msg)
    return windll.user32.CallNextHookEx(None, nCode, WPARAM(wParam), LPARAM(lParam))


HookStruct = genStruct(
    "Hook", pt=genStruct("Point", x=LONG, y=LONG), mouseData=DWORD, flags=DWORD, time=DWORD, dwExtraInfo=PULONG)
msgDict = {v: k for k, v in win32con.__dict__.items() if k.startswith("WM_")}
windll.user32.SetWindowsHookExW(win32con.WH_MOUSE_LL, hookProc, None, 0)
win32gui.PumpMessages()