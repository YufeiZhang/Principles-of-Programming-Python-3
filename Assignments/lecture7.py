# lecture7

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __eq__(felf, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'P({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point(P{}, {})'.format(self.x, self.y)


class Rectangle:
    def __init__(self, pt1, pt2):
        self.pt1 = Point(pt1.x, pt1.y) # you need this because the save reaseon as list of list
        self.pt2 = Point(pt2.x, pt2.y)
        self.area = self._area()

    def _area(self):
        return (abs(self.pt2.x-self.pt1.x) * abs(self.pt2.y-self.pt1.y))
    
    
    def contains(self, pt):
        if pt1.x <= pt2.x:
            if not (pt1.x <= pt.x <= pt2.x):
                return False
            if not (pt1.y <= pt.y <= pt2.y):
                return False
        return True

    
            
            
