from itertools import permutations # 순열 <-> 조합(combination)


def solution(numbers):
    numbers = list(numbers)
    temp = set()
    for i in range(1, len(numbers) + 1):
        alpha = permutations(numbers, i)
        for j in alpha:
            temp.add(int(''.join(j)))

    count = 0
    for alpha in temp:
        if prime_number(alpha) and alpha not in (0, 1):
            count += 1
    return count


def prime_number(alpha):
    for i in range(2, alpha):
        if alpha % i == 0:
            return False
    return True


numbers = '17'
print(solution(numbers))
