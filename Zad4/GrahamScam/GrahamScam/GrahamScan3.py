from matplotlib import pyplot as plt
from random import randint
from math import atan2
import numpy as np

#class Point:
#    def __init__(self,x,y):
#        self.x, self.y = x,y    


#def quicksort(alist):
#	if len(alist)<=1: return alist
#	smaller,equal,larger,q_smaller,q_larger=[],[],[],[],[]
#	pivot=polar_angle(alist[randint(0,len(alist)-1)])
#	for a in alist:
#		p_ang = polar_angle(a)
#		if   p_ang < pivot:  smaller.append(a)
#		elif p_ang == pivot: equal.append(a)
#		else: 				  larger.append(a)
#    q_smaller = quicksort(smaller)
#    q_larger = quicksort(larger)
#	#return   quicksort(smaller) + sorted(equal,key=distance) + quicksort(larger)
#    return q_smaller + q_larger

def quicksort(alist):
    if len(alist) <=1: return alist
    smaller,equal,larger,q_smaller,q_larger = [],[],[],[],[]
    pivot = polar_angle(alist[randint(0,len(alist)-1)])
    for a in alist:
        p_ang = polar_angle(a)
        if p_ang < pivot: smaller.append(a)
        elif p_ang == pivot: equal.append(a)
        else: larger.append(a)

    return quicksort(smaller) + sorted(equal,key=distance) + quicksort(larger)

def polar_angle(p0,p1=None):
    if p1 == None: p1=anchor
    x_span = p0[0] - p1[0]
    y_span = p0[1] - p1[1]
    return atan2(y_span,x_span)

def distance(p0,p1=None):
	if p1 == None: p1=anchor
	y_span = p0[1]-p1[1]
	x_span = p0[0]-p1[0]
	return y_span**2 + x_span**2

def determinant(p0,p1,p2):
    return int(np.linalg.det(np.array([[p0[0],p0[1],1],
                                   [p1[0],p1[1],1],
                                   [p2[0],p2[1],1]])))
def elim_nearer(points):
    angle_sorted = [points[0]]
    for a in angle_sorted[1:]:
        constangle = polar_angle(points[0],a)
        if 

def plot_progress(original_set,hull=None):
    x,y = zip(*original_set)
    plt.scatter(x,y)
    plt.grid()
    if hull != None:
        for h in range(1,len(hull)+1):
            if h == len(hull): h = 0
            p0 = hull[h-1]
            p1 = hull[h]
            plt.plot((p0[0],p1[0]),(p0[1],p1[1]),'r')
    plt.show()

def GrahamScan(points):

    convhull = []

    #1. Selecting element with lowest y-coordinate
    global anchor
    anchor = min(points,key = lambda k: k[1])

    #2. Sorting elements by angle and removing the anchor from original points set
    angle_sorted = quicksort(points)
    #del angle_sorted[angle_sorted.index(anchor)]
    
    convhull=[anchor,angle_sorted[0]]
    for a in angle_sorted[1:]:
        while determinant(convhull[-2],convhull[-1],a) <=0:
            del convhull[-1]
        convhull.append(a)
        plot_progress(points,convhull)
    return convhull

#MAIN THREAD
#points = [[-6,0],[-2,-2],[-2,1],[1,-1],[4,-2],[8,0],[6,2],[10,2],[8,5],[4,5],[7,8],[3,7],[1,9],[-2,6],[-4,9],[-5,6],[4,0]]
#points = [[0,-3],[3,0],[0,3],[-3,0],[0,-2],[2,0],[0,2],[-2,0]]
#points = [[0,1],[0,2],[0,3],[0,4],[0,5]] 
#points = [[1,0],[2,0],[3,0],[4,0],[5,0]]
#points = [[0,0],[24,0],[4,2],[8,2],[9,5],[14,6],[15,30],[18,10],[19,13],[22,16]]
#points = [[0,0],[24,0],[4,2],[8,2],[9,5],[14,6],[15,9],[18,10],[19,13],[22,16]]
points = [[0,0],[1,0],[2,0],[1,1],[2,1],[2,2]]
#points = [[0,0],[11,0],[1,6],[2,2],[3,2],[4,6],[5,2],[6,2],[7,6],[8,2],[9,2],[10,6]]
hull = GrahamScan(points)
print(hull)
#plot_progress(points,hull)

