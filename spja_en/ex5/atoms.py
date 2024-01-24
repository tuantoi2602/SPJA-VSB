import playground
import random

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
        if self.pos_x <= self.size or self.pos_x >= width - self.size:
            self.speed_x *= -1
        if self.pos_y <= self.size or self.pos_y >= height - self.size:
            self.speed_y *= -1


class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        for x in range(count):
            self.atoms.append(self.random_atom())

    def random_atom(self):
        return FallDownAtom(random.randint(1, 100), random.randint(1, 100), random.randint(5, 20),
                            random.randint(5, 20), random.randint(1, 20), playground.Colors.BLUE.value)

    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
        return tuple(ret)


class FallDownAtom(Atom):
    g = 3.0
    damping = 0.8

    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        Atom.__init__(self, pos_x, pos_y, speed_x, speed_y, size, color)

    def move(self, width, height):
        if self.speed_y < 3 and self.speed_y > -3 and self.pos_y >= height - self.size:
            self.speed_y = 0
            self.speed_x = 0
            self.pos_y = height - self.size
        self.pos_x += self.speed_x
        self.speed_y += FallDownAtom.g
        self.pos_y += self.speed_y
        if self.pos_x <= self.size or self.pos_x >= width - self.size:
            self.speed_x *= -1
        if self.pos_y >= height - self.size:
            self.speed_y *= -self.damping
            self.speed_x *= self.damping
        if self.pos_y <= self.size:
            self.speed_y *= -1


if __name__ == '__main__':
    size_x, size_y = 800, 600
    world = ExampleWorld(20, size_x, size_y)
    playground.run((size_x, size_y), world)