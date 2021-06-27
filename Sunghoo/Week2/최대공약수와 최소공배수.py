import math


def solution(n, m):
    alpha = math.gcd(n, m)
    beta = n * m / alpha
    return [alpha, beta]
