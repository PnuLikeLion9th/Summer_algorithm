import math
def solution(left, right):
    answer=0
    for i in range(left,right+1):
        if math.sqrt(i)%1==0:
            i=-i
        answer+=i
    return answer