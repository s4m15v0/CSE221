# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYRWEDXAIAmIedNoIo8zqLPGmCANUDcC
"""

def merge(A,p,q,r): 
    n1=(q-p)+1 
    n2=(r-q) 
    L=[0]*(n1) 
    R=[0]*(n2) 
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2): 
        R[j]=A[q+1+j]

    i=0 
    j=0
    k=p
    while(i<n1 and j<n2): 
        if(L[i]<=R[j]):
            A[k]=L[i]
            i=i+1 
        elif(R[j]<L[i]):
            A[k]=R[j]
            j=j+1 
        k=k+1 
    while(i<n1):
        A[k]=L[i]
        k=k+1 
        i=i+1 
    while(j<n2):
        A[k]=R[j]
        k=k+1
        j=j+1 


def mergesort(A,p,r):
    if p<r: 
        q=int((p+r)/2) 
        mergesort(A,q+1,r) 
        mergesort(A,p,q) 
        merge(A,p,q,r)

n=int(input())
A=[] 

for i in range(0,n):
    temp=int(input())
    A.append(temp)   
mergesort(A,0,n-1) 

print(A)

