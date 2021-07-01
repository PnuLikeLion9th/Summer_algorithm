def solution(x):
    s = str(x)#문자열x로 s에 할당
    sum = 0
    for i in s:#요소 하나씩 돌면서
        sum+= int(i)#sum에 값을 더해준다.
    if x%sum == 0:#x를 sum으로 나누어 나누어 떨어지면 하샤드수 아니면 false를 리턴하라
        return True
    else:
        return False
    