
def solution(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
   # if len(stack) == 0:
   #     answer = 1
   # elif len(stack) != 0:
   #     answer = 0

    return int(stack == [])