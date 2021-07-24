def solution(left, right):
    temp = [gcd(i) for i in range(left, right + 1)]
    numbers = [i for i in range(left, right + 1)]

    return sum(a if b == '+' else -a for a, b in zip(numbers, temp))


def gcd(number: int):
    if sum([1 for j in range(1, number + 1) if number % j == 0]) % 2 == 0:
        return '+'
    else:
        return '-'
