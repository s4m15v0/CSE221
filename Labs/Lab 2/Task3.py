# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WXXOWKPNwjrV25ZRqRiDwti4TKiPDgXu
"""

n=int(input())

ROLL=[]
MARK=[]

for i in range(n):
  ROLL.append(int(input()))
for i in range(n):
  MARK.append(int(input()))
for i in range(1, len(MARK)):
  
  key = MARK[i]
ROLLNO=ROLL[i]
  

j = i-1
while j>=0 and key>MARK[j]:
  MARK[j+1] = MARK[j]
ROLL[j+1]=ROLL[j]
j-=1

MARK[j+1]=key
ROLL[j+1]=ROLLNO

#print
print(ROLL)

file1 = open("input3.txt")
file2 = open("output3.txt","w")


#file read write
for i in ROLL:

  file2.write(i+' ')

file1.close()
file2.close