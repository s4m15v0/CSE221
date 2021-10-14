# -*- coding: utf-8 -*-
"""Lab4Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gAPVGDrHMtyqhVjZtwoEVK52tmA4qsei

Task 2
"""

import heapq
def dijkstra(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(999999)
    dist[source] = 0   # #initialization   
    Q = []   
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
        
    predv = []
    for i in range(len(Graph)+1):
        predv.append(0)
    
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))

    while len(Q) != 0:
        u, l = heapq.heappop(Q)
        
        if visited[l]:
            continue
        
        visited[l] = True
        
        for v in Graph[l]:
            alt = u + v[1]
            
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                predv[v[0]] = l
                heapq.heappush(Q, (dist[v[0]], v[0]))                 
    return predv

Graph_1 = {
    1: []
}

Graph_2 = {
    1: [[2, 10]],
    2: []
}

Graph_3 = {
    3: [[5,1]],
    1: [[2,1], [4,2]],
    2: [[3,4],[5,5]],
    4: [[3,2]],
    5: []
}

w = open('output2.txt','w')

Test_Case_Number_1 = dijkstra(Graph_1, 1)
Test_Case_Number_2 = dijkstra(Graph_2, 1)
Test_Case_Number_3 = dijkstra(Graph_3, 1)

last = len(Graph_1)
w.write("1\n")

last = len(Graph_2)

while last != 1:
    w.write(str(last)+" ")
    last = Test_Case_Number_2[last]
    
w.write("1\n")

last = len(Graph_3)

while last != 1:
    w.write(str(last)+" ")
    last = Test_Case_Number_3[last]
    
w.write("1\n")