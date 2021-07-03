# 1.히샤드 수 

def solution(x):
    y = 0

    for i in str(x):
        y += int(i) #+=: y = y + int(i)
    #x 각각의 값을 더해준 값은 y 
    if x % y == 0:
        return True #x에 y를 나누었을 때 나머지 0이면 True
    else:
        return False #아니면 False

