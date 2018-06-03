import random
import math

#zaladowanie grafu z pliku tekstowego
def load_graph():
    return {int(line.rstrip().split()[0]): [int(i) for i in line.rstrip().split()[1:]] for line in open("source.txt")}    

#drukowanie grafu w postaci wierzcholek:polaczone z nim wierzcholki
def print_graph(graph):
    for k,v in graph.items():
        print(k)
        print(v)

def contract_edge(edge):
    global graph

    #laczenie wierzcholkow z odcietych krawedzi
    v1l = graph[edge[0]]
    v1l.extend(graph[edge[1]])
    del graph[edge[1]]

    #zastapienie wszystkich wystapien v2 przez v1
    for k,l in graph.items():
        graph[k] = [edge[0] if x == edge[1] else x for x in graph[k]]
    
    #usuniecie petli wierzcholka v1 do samego siebie (cech multigrafu)
    graph[edge[0]] = [x for x in graph[edge[0]] if x != edge[0]]

def get_random_edge():
    #wylosowanie dwoch krawedzi v1 i v2, bazujac na polaczeniach od v1
    v1 = list(graph.keys()) [random.randint(0,len(graph)-1)]
    v2 = graph[v1] [random.randint(0,len(graph[v1])-1)]
    return (v1,v2)


minList = []
globalEdges = {}

for x in range(0,20):
    graph = load_graph()
    edges = []
    
    while(len(graph) > 2):
        edge = get_random_edge()
        edges.append(edge)
        contract_edge(edge)
            
    keys = list(graph.keys())
    minlistel = len(graph[keys[0]])
    minList.append(minlistel)
    globalEdges[x] = edges

    minimum = min(minList)
    
#drukowanie rezultatow
print("Liczba powtorzen algorytmu:",20)
print("Poszukiwana minimalna liczba ciec:",minimum)
print("Dokonane ciecia (usuwanie krawedzie)",globalEdges[minimum])