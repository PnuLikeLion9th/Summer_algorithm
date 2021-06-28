def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)  # 각 자리수를 더한다
    # 자릿수의 합으로 x가 나누어 떨어지면 True, 아니면 False 반환
    return True if x % sum == 0 else False
