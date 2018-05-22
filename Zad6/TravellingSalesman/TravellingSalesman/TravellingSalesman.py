import itertools
import math

##points = [[2,2],[6,4],[4,7],[8,8]]
points = [[2, 5],
              [7, 5],
              [2, 1],
              [7, 1]]


def lenght(p1,p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx**2 + dy**2)

def distances(points):
    return [[lenght(x,y) for y in points] for x in points]

def solve_tsp(points):
    #all_distances = distances(points)
    all_distances = [[0,1,15,6],[2,0,7,3],[9,6,0,12],[10,4,8,0]]
    parents = set()
    A = {(frozenset([0,idx+1]), idx+1): (dist,[0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2,cnt):
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1,cnt),m)]:
            for j in S - {0}:
                A[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j],A[(S-{j},k)][1] +[j]) for k in S if k != 0 and k != j])
                #tu generalnie widzę już, jakie sa wyniki i podzbiory, S przeszukiwany podzbiór
                print(A[(S,j)])
    
    #trzeba by znalezc indeks, podzbior, ktory odpowiada za kolejnosc poprawnej trasy
    #ponadto, trzeba wybierac dobre rozwiazanie tylko z tych najdluzszych lancuchow, trzeba porownac z cnt (te podzbiory brac pod uwage)
    print("Printing with iter:")
    [print([A[d][1]]) for d in iter(A)]
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[0]

tour = solve_tsp(points)
print(tour)


