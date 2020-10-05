class Cylinder:

    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v = Cylinder.pi * (self.radius ** 2) * self.height
        print(v)

    def surface_area(self):
        s_a = (Cylinder.pi * 2 * self.radius * self.height) + (2 * Cylinder.pi * (self.radius ** 2))
        print(s_a)

c = Cylinder(2,3)
c.volume()
c.surface_area()