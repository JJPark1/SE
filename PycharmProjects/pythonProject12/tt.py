import heapq
import sys
heap =[]
n=int(sys.stdin.readline())

while n>0:
    a=int(sys.stdin.readline())
    if a>0:
        heapq.heappush(heap,a)
    elif a==0:
        try:
            print(heapq.heappop(heap))
        except:
            print("0")
    n-=1



