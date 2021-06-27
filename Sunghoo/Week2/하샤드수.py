def solution(x):
    div_sum = sum([int(i) for i in str(x)])
    return x % div_sum == 0
