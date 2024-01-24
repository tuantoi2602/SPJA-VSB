import playground
import random
import xml.etree.ElementTree as ET

class Atom(object):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.size = float(size)
        self.speed_x = float(speed_x)
        self.speed_y = float(speed_y)
        self.color = color

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x + self.size > width:
            self.speed_x = -self.speed_x
            self.pos_x = width - self.size
        if self.pos_x < self.size:
            self.speed_x = -self.speed_x
            self.pos_x = self.size

        if self.pos_y + self.size > height:
            self.speed_y = -self.speed_y
            self.pos_y = height - self.size
        if self.pos_y < self.size:
            self.speed_y = -self.speed_y
            self.pos_y = self.size

class FallDownAtom(Atom):
    g = 3.0
    damping = 0.8
    
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        Atom.__init__(self, pos_x, pos_y, speed_x, speed_y, size, color)
    
    def move(self, width, height):
        self.speed_y += FallDownAtom.g
        
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x + self.size > width:
            self.speed_x = -self.speed_x
            self.pos_x = width - self.size
        if self.pos_x < self.size:
            self.speed_x = -self.speed_x
            self.pos_x = self.size

        if self.pos_y + self.size > height:
            self.speed_x = self.speed_x*FallDownAtom.damping
            self.speed_y = self.speed_y*FallDownAtom.damping
            self.speed_y = -self.speed_y
            self.pos_y = height - self.size
        if self.pos_y < self.size:
            self.speed_y = -self.speed_y
            self.pos_y = self.size
        

class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        self.load_from_xml('atoms.xml')

    def load_from_xml(self, filename):
        root = ET.parse(filename)
        world = root.find('world')
        self.size_x = world.attrib['sizeX']
        self.size_y = world.attrib['sizeY']
        atoms = root.findall('atom')
        for atom in atoms:
            type_atom = atom.attrib['type']
            color = atom.find('color').text
            pos_x, pos_y = atom.find('position').text.split(',')
            radius = atom.find('radius').text
            veloc_x, veloc_y = atom.find('velocity').text.split(',')
            if type_atom == 'FallDown':
                self.atoms.append(FallDownAtom(pos_x,pos_y,veloc_x,veloc_y,radius,color))
            else:
                self.atoms.append(Atom(pos_x,pos_y,veloc_x,veloc_y,radius,color))

    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
        return tuple(ret)
    
    def get_size(self):
        return (self.size_x, self.size_y)

    def __str__(self):
        count_atom = 0
        count_falldown = 0
        for atom in self.atoms:
            if type(atom).__name__ == "Atom":
                count_atom += 1
            if type(atom).__name__ == "FallDownAtom":
                count_falldown += 1
        return "World size={}x{}\n " \
               "Number of normal atoms = {}\n " \
               "Number of falldown atoms = {}".format(self.size_x, self.size_y, count_atom, count_falldown)


if __name__ == '__main__':
    size_x, size_y = 800, 600
    world = ExampleWorld(10, size_x, size_y)
    print(world)
    playground.run(world.get_size(), world)
