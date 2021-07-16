def solution(a, b):
    li = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    return day[(sum(li[:a]) + b) % 7]
