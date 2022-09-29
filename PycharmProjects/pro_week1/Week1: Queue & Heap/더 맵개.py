import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0]<k:
        if scoville[0] < k and len(scoville) == 1:
            answer = -1
            break
        mix= heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, mix)
        answer += 1
    return answer


s = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(s, k))
