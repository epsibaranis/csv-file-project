# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:53:52 2022

@author: tt
"""
import csv
def studentsper(x,y):
    l=len(y)
    #print(y[6])
    b=[]
    for i in range(0,2):
        b.append(y[i])
        if y[i]!='Kanniyakumari' and y[i]!='Thiruvannamalai':
          b.append('')
        if y[i]=='Chennai' or y[i]=='Salem':
            b.append(' ')
    b.append('')
    """for i in range(3,4):
         b.append(y[i])
         b1=len(y[i])
         if b1>=16 and b1<=19:
             b.append('')
             b.append('')
             b.append('')
         if b1>=20 and b1<=23:
          b.append('')
          b.append('')
         if b1>=24 and b1<=26:
          b.append('')"""
    for j in range(4,6):
        b.append(y[j])
        b.append('')
        b.append('')
    for j in range(6,11):
        b.append(y[j])
        b.append('')
    for i in range(11,16):
        b.append(y[i])
        b.append('')
    for i in range(9,8,-1):
       q=y[i]/5
       b.append(q)
    for i in b:
        print(i,end='\t')
    print()
#main        
f=open('studentsmarksheet.csv')
t=csv.reader(f)
z=[]
x=next(t)
x.append('total')
x.append('')
x.append('H.M.T')
x.append('H.M.E')
x.append('H.M.M')
x.append('H.M.S')
x.append('H.M.S.S')
x.append('rank')
x.append('percentage')
l=len(x)
for i in range(0,2):
    z.append(x[i])
    z.append('')
z.append('')
#z.append('\t')
"""for i in range(3,4):
    z.append(x[i])
    z.append('')
    z.append('')
    z.append('')
    z.append('\t\t')"""
for i in range(4,l):
    z.append(x[i])
    if x[i]=='English':
     z.append('')
    #z.append('')
for i in z:
 print(i,end='\t')
print()
a=[]
for i in t:
   a.append(i)
b2=0
b3=0
b4=0
b5=0
b6=0
for i in range(len(a)):
    m1=0
    l1=len(a[i])
    for j in range(4,l1):
        m1=m1+int(a[i][j])
    a[i].append(m1)
    for j in range(4,5):
        if b2<int(a[i][j]):
            b2=int(a[i][j])
    for j in range(5,6):
        if b3<int(a[i][j]):
            b3=int(a[i][j])
    for j in range(6,7):
        if b4<int(a[i][j]):
            b4=int(a[i][j])
    for j in range(7,8):
        if b5<int(a[i][j]):
            b5=int(a[i][j])
    for j in range(8,9):
        if b6<int(a[i][j]):
            b6=int(a[i][j])
for y in range(len(a)):
    a[y].append(b2)
    a[y].append(b3)
    a[y].append(b4)
    a[y].append(b5)
    a[y].append(b6)
l2=len(a[0])
#print(l2)
a.sort(key=lambda rank:rank[9],reverse=True)
m=1
m2=0
for y in a:
    l=len(y)
    #print(m2)
    if m2==y[9]:
        y.append(m1)
        n1=studentsper(x,y)
    else:
        y.append(m)
        n1=studentsper(x,y)
        m2=y[9]
        m1=m
        m+=1


