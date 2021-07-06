def solution(n):
    answer = 0
    for i in range(1, n+1):  # 1부터 n까지 돌며 약수가 아닌 수는 continue, 약수인 수는 answer에 더해짐
        if n % i:
            continue
        answer += i
    return answer

# list comprehension 풀이


def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])
