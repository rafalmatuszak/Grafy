from operator import attrgetter
import csv
import matplotlib.pyplot as plt
import sys

#Point class definition
class Point(object):
    '''
        Class definition for Cartesian points
    '''
    def __init__(self,x,y):
        self.x, self.y = x, y

    def __str__(self):
        return "P"

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    
#Node class definition
class Node(object):
    '''
        Class definition for tree nodes
    '''
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "Node id: %s" % (self.id)

#traverse tree printing
def traverse(rootnode):
  thislevel = [rootnode]
  depth, p = 0, 0
  a = ' '*100
  while thislevel:
    nextlevel = []
    a = a[:len(a) // 2]
    for n in thislevel:
      if isinstance(n.id,Point):
        print(a + str(n.id) + str(p),end ='')
        p += 1
      else:
        print(a + 'l' + str(depth) + a,end='')
        depth += 1

      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
      thislevel = nextlevel
    print("\n")

#def traverse2(rootnode):
#    this = [rootnode]
#    global depth
#    p = 0
#    a =  ' '*100
#    while this:
#        nextlevel = []
#        for n in this:
#            if isinstance(n.id,Point):
#                print("\t" + '-' + str(n.id) + str(p))
#            else:
#                print("\t" + '+' + 'l' + str(depth))        
#                depth += 1
#            if n.left: nextlevel.append(n.left)
#            if n.right: nextlevel.append(n.right)
#            this = nextlevel
#        print("\n")

#Calculating median    
def mediann(P):
        length = len(P)
        eve = length // 2
        if length % 2 == 0:
            return Point(P[(length // 2) - 1].x,P[(length // 2) - 1].y)
        else:
            return Point(P[length // 2].x,P[length // 2].y)

#Comparition functions for x and y coordinates
def compare(a,b,attr): 
    if attr == 'x':
        return True if a.x > b.x else False
    elif attr == 'y':
        return True if a.y > b.y else False
    else:
        sys.exit("Wrong attribute! Exiting...")

#method for buildiing KD Tree
def buildKDTree(points,depth = 0,label='l'):
    p_right = []
    p_left = []

    if points == []:
        return

    if depth % 2 == 0:
        points.sort(key=attrgetter('x'))
        med = mediann(points)
        print("Dividing by x axis with median: ",med.x,med.y)
        for it in points:
            p_right.append(it) if compare(it,med,'x') == True else p_left.append(it)

    else:
        points.sort(key=attrgetter('y'))
        med = mediann(points)
        print("Dividing by y axis with median: ",med.x,med.y)
        for it in points:
            p_right.append(it) if compare(it,med,'y') == True else p_left.append(it)
    
    #binding node
    label += str(depth)
    node = Node(label,None,None)
    if (len(p_left) == 1) & (len(p_right) == 1):
        node.left, node.right = Node(Point(p_left[0].x,p_left[0].y),None,None),Node(Point(p_right[0].x,p_right[0].y),None,None)
        node.id = label
    elif len(p_left) == 1:
        node.left = Node(Point(p_left[0].x,p_left[0].y),None,None)
        node.right = buildKDTree(p_right,depth+1);
        node.id = label
    elif len(p_right) == 1:
        node.right = Node(Point(p_right[0].x,p_right[0].y),None,None)
        node.left = buildKDTree(p_left,depth+1);
        node.id = label
    else:   
        node.left = buildKDTree(p_left,depth + 1)
        node.right = buildKDTree(p_right,depth + 1)
    
    return node

#loading points from CSV file    
points = []
with open('points.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        points.append(Point(int(row['x']),int(row['y'])))

#preparing figure and drawing points
x,y = [],[]

for p in points:
    x.append(p.x)
    y.append(p.y)

plt.axis([0,40,0,40])
plt.grid()
plt.scatter(x,y)
#plt.show()

root = buildKDTree(points,0)
traverse(root)
#traverse2(root)
