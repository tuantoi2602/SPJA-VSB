import playground
from random import randint

class ExampleWorld(object):
    def __init__(self, size_x, size_y, number_atoms):
        self.width = size_x
        self.height = size_y
        self.number_atoms = []
        self.atom_size_limits = (5,30)
        self.atom_vel_limits = (1,10)

        for i in range(number_atoms):
            r = randint(self.atom_size_limits[0], self.atom_size_limits[1])
            x = randint(r, self.width - r)
            y = randint(r, self.height - r)
            vx = randint(self.atom_vel_limits[0], self.atom_vel_limits[1])
            vy = randint(self.atom_vel_limits[0], self.atom_vel_limits[1])
            self.number_atoms.append(Atom(x, y, vx, vy, r))

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.
        return: tuple of atom objects, each containing (x, y, radius) coordinates
        """
        for i in self.number_atoms:
            i.move(self.width, self.height)
            yield i.to_tuple()

class Atom():
    def __init__(self, x, y, vx, vy, r):
        self._x = x
        self._y = y
        self._r = r
        self._vx = vx
        self._vy = vy

    def to_tuple(self):
        return(self._x,self._y,self._r)

    def move(self, size_x, size_y):
        if (self._x + self._r) >= size_x or (self._x - self._r) <= 0:
            self._vx *= -1
        if (self._y + self._r) >= size_y or (self._y - self._r) <= 0:
            self._vy *= -1
        self._x += self._vx
        self._y += self._vy



if __name__ == '__main__':
    size_x, size_y = 800, 600

    world = ExampleWorld(size_x, size_y,20)
    playground.run((size_x, size_y), world)
