
import sys
n= int(sys.stdin.readline())
l =[]
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))

l.sort(key = lambda x: (x[0],x[1]))

for i in l:
    print(i[0],i[1])
'''
n=int(input())

l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))


f=sorted(l,key = lambda x: (x[0],x[1]))

for i in range(n):
    print(f[i][0],f[i][1]) '''
