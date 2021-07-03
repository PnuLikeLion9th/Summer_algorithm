def solution(n):
    count = 0
    for i in range(1, n):
        total = 0
        for j in range(i, n):
            total += j
            if total == n:
                count += 1
                break
            elif total > n:
                break
    return count + 1

# 다른 사람 풀이
def solution(num):
    return len([i for i in range(1, num + 1, 2) if num % i is 0])
