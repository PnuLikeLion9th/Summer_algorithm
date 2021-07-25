# sol1) deque 이용
from collections import deque


def solution(prices):
    answer = []

    que = deque(prices)
    while que:
        price = que.popleft()
        cnt = 0
        for n in que:
            cnt += 1
            if n < price:  # que에서 뽑아낸 수보다 n이 작으면 break
                break
        answer.append(cnt)

    return answer


# sol2) Brute Force
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
