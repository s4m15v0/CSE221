# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cRQe20F7KtYP5SPIlIMHuoc8q6_XvHic
"""

def BubbleSort(arr):
    for i in range(len(arr)-1):
        bubble=0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                bubble=1
                #swap( arr[j+1], arr[j] )
                arr[j+1], arr[j]=arr[j], arr[j+1]
        if bubble==0:
            break

f1=open('/content/input1.txt')
f2=open('/content/output1.txt','w')


n=(f1.readline())
arr=list(map(int,f1.readline().split()))
BubbleSort(arr)

for i in arr:
    f2.write(str(i)+' ')


f1.close()
f2.close()

#another process


a = []
number = int(input("Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Enter the %d Element of List1 : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp

print("sorted List : ", a)
