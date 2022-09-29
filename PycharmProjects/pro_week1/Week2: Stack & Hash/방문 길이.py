from collections import deque

def solution(dirs):
    dirs = deque(dirs)
    start = [0,0]
    stack =[]
    for i in range(0, len(dirs)):
        temp = [0, 0]

        key = dirs.popleft()
        print(key)
        if key == 'U':
            start[1] += 1
            temp = start
            stack.append(temp)
            temp=[0,0]
        elif key == 'D':
            start[1] -= 1
            temp = start
            stack.append(temp)
            temp = [0, 0]
        print(stack)

    return len(stack)

dirs = "UUUDD"
print(solution(dirs))