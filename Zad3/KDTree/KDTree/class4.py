class Point:
    '''
        Class definition for Cartesian points
    '''
    def __init__(self,x,y):
        self.x, self.y = x, y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

P1 = Point(2,4)
i = 5
type(P1)
type(i)