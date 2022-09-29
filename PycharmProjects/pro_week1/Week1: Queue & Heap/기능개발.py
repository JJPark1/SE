
def solution(progresses, speeds):
    answer = []
    progresses_queue = progresses
    while len(progresses_queue) > 0:
        for x in range(0, len(progresses_queue)):
            progresses[x] += speeds[x]
        temp = 0
        count = 0

        while True:
            if(len(progresses_queue) ==0):
                break
            print("list",progresses_queue)
            if progresses_queue[0]>=100:
                print("Pop",progresses_queue.pop(0))
                speeds.pop(0)
            else:
                break
            count+=1

        if(count>=1):
            print("ok")
            answer.append(count)
    print(answer)
    return answer


print("hi")
print(solution([93,30,55],[50,30,15]))