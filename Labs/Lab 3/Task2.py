# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8loeDaz1Hv0CWTHcrveQcn_UlMIxt9S
"""

a ={
    1 : [2],
    2 : [3, 4, 5], 
    3 : [4, 7, 11],
    4 : [],        
    5 : [6, 7],    
    6 : [7, 8],    
    7 : [11],      
    8 : [9, 10],   
    9 : [10],
    10 : [11],
    11 : [12],
    12 : []
}

def bfs(v, g, n, e):
    
    wf2 = open('/content/input2.txt','w')
    wf2.write("Places:")
    
    q = []
    v[int(n)-1] = 1
    q.append(n)
    
    length = len(q)
    
    while length != 0:
        x = q.pop(0)
        wf2.write(" "+str(x)+" ")
        
        if int(x) == int(e):
            break
        
        for n in g[int(x)]:
            if v[int(n)-1] == 0:
                v[int(n)-1] = 1
                q.append(n)
                
visited = [0] * 12
bfs(visited, a, "1", "12")