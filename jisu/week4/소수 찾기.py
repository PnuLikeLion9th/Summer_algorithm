# 핵심: 에라토스테네스의 체로 풀기

def solution(n):
    answer = 0
    arr = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if arr[i] == True:
            for j in range(2*i, n+1, i):  # 배수일 경우 False
                arr[j] = False

    for i in arr:
        if i == True:
            answer += 1
    return answer


# 간결한 코드
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)
