def solution(s):

    count = 0
# ())(
    for x in s:
        if x=='(':
            count+=1
        elif x ==')':
            count-=1

        if(count<0):
            return False
    if(count==0):
        return True
    else:
        return False






