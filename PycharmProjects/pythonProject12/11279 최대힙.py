import heapq
import sys
n=int(input())
heap =[]


for i in range(n):
    a=int(sys.stdin.readline())
    if a>0:
        heapq.heappush(heap,(-a))
    elif a==0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
