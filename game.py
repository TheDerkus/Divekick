from win32gui import FindWindow, SetForegroundWindow, ShowWindow, GetForegroundWindow, GetWindowText
from win32con import SW_MAXIMIZE
from pymem import Pymem
from pymem.process import module_from_name

class Game:

    TITLE = 'Divekick (D3D11)'
    EXE = 'DivekickD3D11'

    def __init__(self):
        dh = FindWindow(None, self.TITLE)
        ShowWindow(dh, SW_MAXIMIZE)
        SetForegroundWindow(dh)
        self.dk = Pymem(self.EXE)
        hnd = self.dk.process_handle
        self.base = module_from_name(hnd, self.EXE + '.exe').lpBaseOfDll

    def active(self):
        return GetWindowText(GetForegroundWindow()) == self.TITLE
