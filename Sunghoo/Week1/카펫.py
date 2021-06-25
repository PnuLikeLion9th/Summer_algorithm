brown = 24
yellow = 24


def solution(brown, yellow):

    sum = brown + yellow # = a*b

    for i in range(1, yellow + 1):

        if yellow % i == 0:
            m = yellow // i
            n = i
            print(m, n)
            if (m + 2) * (n + 2) == sum:
                if m >= n:
                    return [m + 2, n + 2]
                else:
                    return [n + 2, m + 2]
