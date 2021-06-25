number = '1231234'
k = 3


def solution(number, k):
    result = []

    for idx, i in enumerate(number):
        while len(result)>0 and i > result[-1] and k > 0:
            result.pop()
            k -= 1

        if k == 0:
            result += list(number[idx:])
            break

        result.append(i)
    result = result[:-k] if k > 0 else result

    return ''.join(result)
