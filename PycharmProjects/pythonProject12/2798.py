import itertools


n,m=map(int,input().split())
num = list(map(int,input().split()))

per_arr=itertools.permutations(num,3)
max = 0
for i in per_arr:
    if(i[0]+i[1]+i[2]> max and i[0]+i[1]+i[2] <= m):
        max=i[0]+i[1]+i[2]

print(max)
