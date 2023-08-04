
class Fight:

    breadcrumbs = [
        ([0x4, 0xC, 0x48, 0x4, 0x19C, 0x34, 0x48], 0x2FED8C), # time
        ([0x4, 0xC, 0x48, 0x8, 0x4, 0x600], 0x2FED8C), # p1x
        ([0x4, 0xC, 0x50, 0x138, 0x4, 0x554], 0x2FED8C), # p1y
        ([0x4, 0xC, 0x50, 0x4, 0x3F0, 0xC8], 0x2FED8C), # p2x
        ([0x4, 0xC, 0x48, 0x4, 0xA0, 0x4, 0x710], 0x2FED8C), #p2y
        ([0x4, 0xC, 0x4C, 0x0, 0x198, 0x18, 0x2A0], 0x2FED8C), # can_move
        ([0x20, 0x4, 0x4, 0x4, 0xA0, 0x0, 0x204], 0x2FFD50), # p1frame
        ([0x20, 0x4, 0x4, 0x4, 0xA0, 0x4, 0x204], 0x2FFD50), # p2frame 0x204
        ([], 0x2FFD88), # is_paused
        ([0x4, 0xC, 0x50, 0x698], 0x2FED8C), # p1wins
        ([0x4, 0xC, 0x50, 0x4, 0x3F0, 0x71C], 0x2FED8C), # p2wins
        ([0x4, 0xC, 0x50, 0x6BC], 0x002FED8C), # p1meter
        ([0x4, 0xC, 0x50, 0x528, 0x740], 0x002FED8C), # p2meter
    ]

    def __init__(self, g):
        self.dk = g.dk
        self.base = g.base
        self.addresses = list(self.address(b) for b in self.breadcrumbs)

    def address(self, breadcrumb):
        crumbs, magic = breadcrumb
        a = self.base + magic
        for b in crumbs:
            a = self.dk.read_uint(a) + b
        return a

    def reset_meter(self):
        ads = self.addresses
        self.dk.write_float(ads[11], 0.0)
        self.dk.write_float(ads[12], 0.0)

    def reset_wins(self):
        ads = self.addresses
        self.dk.write_int(ads[9], 0)
        self.dk.write_int(ads[10], 0)

    def state(self):
        self.reset_meter()
        ads = self.addresses
        int_ = self.dk.read_int
        float_ = self.dk.read_float
        bool_ = self.dk.read_bool
        return {
            'time': int_(ads[0]),
            'p1x': float_(ads[1]),
            'p1y': float_(ads[2]),
            'p2x': float_(ads[3]),
            'p2y': float_(ads[4]),
            'can_move': bool_(ads[5]),
            'p1frame': int_(ads[6]),
            'p2frame': int_(ads[7]),
            'is_paused': bool_(ads[8]),
            'p1wins': int_(ads[9]),
            'p2wins': int_(ads[10]),
        }
