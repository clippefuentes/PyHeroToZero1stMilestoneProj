class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        pass

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        d = ((x2 - x1)**2 + (y2- y1)**2) ** 0.5
        print(d)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        s = (y2 - y1)/(x2 - x1)
        print(s)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()