from operator import attrgetter
from math import atan2,pi
import csv

#Point class definition
class Point(object):
    '''
        Class definition for Cartesian points
    '''
    def __init__(self,x,y,angle_ratio=None,dist=None):
        self.x, self.y, self.angle_ratio, self.dist = x, y, angle_ratio, dist

    def __str__(self):
        return "(%s,%s,%s,%s)" % (self.x,self.y,self.angle_ratio,self.dist)

    def __repr__(self):
        return "Point(%s, %s, %s)" % (self.x, self.y, self.angle_ratio,self.dist)

#Graham scam algorithm

def GrahamScan(points):
    
    #list containting points of calculated convex hull
    hull = []

    #1. Selecting element with lowest y-coordinate
    yspoints = sorted(points,key = attrgetter('x'))
    anchor = min(yspoints,key = attrgetter('y'))
    idx = points.index(anchor)

    #2. Removing anchor element from global points set.
    #Copying points to separate list, calculate angle_ration and sort them in reverse order
    points2 = list(points)
    points2.pop(idx)

    for p in points2:
        span_x = p.x - anchor.x
        span_y = p.y - anchor.y
        if span_x == 0:
            p.angle_ratio = float('Inf')
        else: 
            p.angle_ratio = float(span_y/span_x)
        p.dist = span_x**2 + span_y**2
        #p.angle_ratio = float((atan2(span_y,span_x))*180/pi)
        
    points2.sort(key=attrgetter('angle_ratio'),reverse = True)

    for p in points2: print(p)

    return anchor   


points = []
with open('points.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        points.append(Point(int(row['x']),int(row['y'])))

GrahamScan(points)
