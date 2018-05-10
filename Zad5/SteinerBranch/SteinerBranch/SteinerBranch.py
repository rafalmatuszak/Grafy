from matplotlib import pyplot as plt
from operator import itemgetter, attrgetter
import itertools as iter


class Point(object):
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.met = self.x + self.y    

    def __repr__(self):
        return("(%s,%s)") % (self.x,self.y)

    def __str__(self):
        return("(%s,%s)") % (self.x,self.y)

class MergedPoint(object):
    def __init__(self,x,y):
        if(met(x) == met(y)):
            self.P = x if x.x < y.x else y
            self.Q = y if x.x < y.x else x
        else:
            self.P = x if met(x) < met(y) else y
            self.Q = y if met(x) < met(y) else x
        
        self.Merge = Point(min(self.P.x,self.Q.x),min(self.P.y,self.Q.y))
        self.met = met(self.Merge)
        self.cost = cost(self.P,self.Q)

    def __repr__(self):
        return("(%s,%s)" % (self.Merge.x,self.Merge.y))

def met(a):
    return a.x + a.y

def cost(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)
   


#points = [Point(0,0),Point(4,7),Point(7,7),Point(3,4),Point(5,4),Point(7,4),Point(5,2),Point(9,2)]
#points = [Point(0,0),Point(0, 2),Point(2, 6),Point(3, 2),Point(3, 5),Point(3, 7),Point(5, 2),Point(5, 4),Point(7, 6),Point(8, 2),Point(8, 3),Point(8, 5),Point(10, 1),Point(12, 3)]
points = [Point(0,0), Point(0,8), Point(1,7), Point(2,6), Point(3,5),Point(4,4),Point(5,3),Point(6,2), Point(7,1)]
points2 = list(points) 

#porzadek poczatkowy
points.sort(key=attrgetter('y'),reverse=True)
points.sort(key=attrgetter('met'),reverse=True)    

def ApproxRSA(points):
    merges = []
    while (len(points) > 1):
        bMerge = MergedPoint(points[0],points[1])
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                merged = MergedPoint(points[i],points[j])
                if((merged.met >= bMerge.met) and (merged.cost < bMerge.cost)):
                    bMerge = merged
        merges.append(bMerge)
        idx = points.index(bMerge.Q)
        del points[idx]
        idx2 = points.index(bMerge.P)
        points[idx2] = bMerge.Merge
    
    return merges

def drawRSA(points,merges):
    x,y=[],[]
    x=[p.x for p in points]
    y=[p.y for p in points]
    plt.scatter(x,y,color='red')
    for m in merges:
        plt.plot((m.Merge.x,m.P.x),(m.Merge.y,m.P.y),'r')
        plt.plot((m.Merge.x,m.Q.x),(m.Merge.y,m.Q.y),'r')
    #plt.plot((0,merge_points[-1].Merge.x),(0,merge_points[-1].Merge.y),'r')
    #plt.plot((merge_points[-1].Merge.x,0),(merge_points[-1].Merge.y,0),'r')
    plt.grid()
    plt.show() 
         

merge_points = ApproxRSA(points)
drawRSA(points2,merge_points)
