import csv
import numpy as np
from operator import attrgetter

#point class for keeping polygon 
class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y    

def isOrientationRight(cur, cons, prec):
    mat = np.array([[cons.x,cons.y,1],[cur.x, cur.y, 1],[prec.x, prec.y, 1]])
    if(np.linalg.det(mat) > 0):
        return True
    else:
        return False
    
def isMaximum(cur,cons,prec):
    if((cur.y > cons.y) & (cur.y > prec.y)):
        return True
    else:
        return False

def isMinimum(cur,cons,prec):
    if((cur.y < cons.y) & (cur.y < prec.y)):
        return True
    else:
        return False

#verticies list declaration
verticies = []
maximas = []
minimas = []

#loading list of verticies from file
with open('points.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        verticies.append(Point(int(row['x']),int(row['y']))) 

#main program
#iterating over verticies; start parameters
for v in range(0,len(verticies)):
    cur = Point(verticies[v].x,verticies[v].y)
    if(v == len(verticies)-1):
        conss = Point(verticies[1].x,verticies[1].y)
        cons = Point(verticies[0].x,verticies[0].y)
        prec = Point(verticies[v-1].x,verticies[v-1].y)
        precc = Point(verticies[v-2].x,verticies[v-2].y)
    else:
        if(v == len(verticies)-2):
            conss = Point(verticies[0].x,verticies[0].y)
        else:
            conss = Point(verticies[v+2].x,verticies[v+2].y)
            cons = Point(verticies[v+1].x,verticies[v+1].y)
            prec = Point(verticies[v-1].x,verticies[v-1].y)
            precc = Point(verticies[v-2].x,verticies[v-2].y)
    
    #checking collinearity
    if(cur.y == prec.y):
        prec = precc 
    elif(cur.y == cons.y):
        cons = conss

    if(isMaximum(cur,cons,prec) & isOrientationRight(cur,cons,prec)):
        maximas.append(cur)
    elif(isMinimum(cur,cons,prec) & isOrientationRight(cur,cons,prec)):
        minimas.append(cur)
    else:
        continue

min_num = min(minimas,key=attrgetter('y'))
max_num = max(maximas,key=attrgetter('y'))

#protection for max-min y coordinate difference
if(len(minimas) == 0 | len(maximas) == 0 | min_num.y < max_num.y):
    print("There is no {O}-Kernel, because local minimum is lower placed than local maximum");
else:
	print("Kernel of given polygon is located between below shown points: ")
    print("Minimum:")
    print(min_num.x,min_num.y)
    print("Maximas:")
    print(max_num.x,max_num.y)
 