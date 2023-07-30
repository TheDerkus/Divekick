from win32gui import FindWindow, SetForegroundWindow, ShowWindow
import time
from win32con import SW_MAXIMIZE
import pymem
from pymem import Pymem
from pymem.process import module_from_name

class Game:

    def __init__(self):
        dh = FindWindow(None, 'Divekick (D3D11)')
        ShowWindow(dh, SW_MAXIMIZE)
        SetForegroundWindow(dh)
        self.dk = Pymem('DivekickD3D11')
        hnd = self.dk.process_handle
        self.base = module_from_name(hnd, 'DivekickD3D11.exe').lpBaseOfDll
