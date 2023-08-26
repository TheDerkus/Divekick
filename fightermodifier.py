import xml.etree.ElementTree as ET

PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Divekick\\data\\source\\Other\\CharacterData\\Dive\\data.xml"

class FighterModifier:

    def __init__(self, p):
        self.path = p
        self.data = None

    def no_headshots(self):
        headBoxes = self.data.findall('./hitboxes/playerAction/charFrame/headBox')
        for hb in headBoxes:
            hb.tag = 'hurtBox'

    def no_meter(self):
        self.data.getroot().find('kPerKick').text = '0.0'

    def tostring(self):
        return ET.tostring(self.data.getroot(), encoding='unicode')

    def read(self):
        with open(self.path, 'r') as file:
            self.data = ET.parse(file)

    def modify(self):
        self.read()
        self.no_meter()
        self.no_headshots()
        self.write()

    def write(self):
        xml = self.tostring()
        with open(self.path, 'w') as file:
            file.write(xml)


FighterModifier(PATH).modify()
