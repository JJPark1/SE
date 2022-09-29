from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = deque(skill)
        for s in skill_tree:
            if s in skill and s != skill_list.pop():
                break
        else:
            answer+=1
    return answer
