import sys

n=int(sys.stdin.readline())

l1=set(map(int,input().split()))

m=int(sys.stdin.readline())
l2=list(map(int,input().split()))

for i in l2:
    if i in l1:
        print("1")
    else:
        print("0")

