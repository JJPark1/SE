import heapq

def solution(no, works):
    result = 0
    heapq.heapify(works)

    for _ in range(0, no):
        heapq.heappush(heap,(-))
        works[-1] += -1


    for i in works:
        result += i*i



    return result
