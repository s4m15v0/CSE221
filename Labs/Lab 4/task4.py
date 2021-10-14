# -*- coding: utf-8 -*-
"""Lab4Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oqoiaapo1Vgswv9KGfoOUdfNy9wTj9FK

Task 4
"""

import heapq
def Network(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(-999999)
    dist[source] = 0 #initialization
    
    Q = []
    
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
        
    predv = []
    for i in range(len(Graph)+1):
        predv.append(0)
    predv[source] = 1
    
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))
        
    heapq._heapify_max(Q)
        
    while len(Q) != 0:
        u, l = heapq._heappop_max(Q)
        
        if visited[l] == 1:
            continue
        
        visited[l] = 1
        
        for v in Graph[l]:
            alt = 0
            
            if u == 0:
                alt = v[1]
            elif v[1] == 0:
                alt = u
            elif u < v[1]:
                alt = u
            else:
                alt = v[1]
                
            if alt > dist[v[0]]:
                dist[v[0]] = alt
                predv[v[0]] = l
                
                heapq.heappush(Q, (dist[v[0]], v[0]))
                heapq._heapify_max(Q)
                
    return dist

S_1 = 1
Graph_1 = {
    1: []
}

S_2 = 1
Graph_2 = {
    1: [[2,1]],
    2: []
}

S_3 = 2
Graph_3 = {
    1: [[2,1]],
    2: []
}

S_4 = 1
Graph_4 = {
    3: [[2,6], [4,2]],
    1: [[2,3], [3,8]],
    2: [[4,7]],
    4: []
}

w = open("output4.txt", "w")

Test_Case_Number_1 = Network(Graph_1, S_1)
Test_Case_Number_2 = Network(Graph_2, S_2)
Test_Case_Number_3 = Network(Graph_3, S_3)
Test_Case_Number_4 = Network(Graph_4, S_4)

w.write(str(Test_Case_Number_1[-1])+"\n")

Test_Case_Number_2 = Test_Case_Number_2[1:]
for i in Test_Case_Number_2:
    w.write(str(i)+" ")
w.write("\n")

Test_Case_Number_3 = Test_Case_Number_3[2:]
w.write(str("-1")+" ")
for i in Test_Case_Number_3:
    w.write(str(i)+"\n")
    
Test_Case_Number_4 = Test_Case_Number_4[1:]
for i in Test_Case_Number_4:
    w.write(str(i)+" ") 
w.write("\n")