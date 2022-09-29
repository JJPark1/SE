def solution(n, works):
    answer = 0
    for _ in range (0,n):
        works.sort()
        print("배열",works)
        if(works[-1]!=0):
            works[-1]+=-1
    for x in works:
        answer+=x*x
    return answer
