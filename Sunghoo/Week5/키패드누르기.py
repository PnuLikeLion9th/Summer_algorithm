def solution(numbers, hand):
    if hand == 'right':
        hand = 'R'
    else:
        hand = 'L'

    left = (1, 4, 7)
    right = (3, 6, 9)
    answer = ''
    key = {1: (0, 0),
           2: (0, 1),
           3: (0, 2),
           4: (1, 0),
           5: (1, 1),
           6: (1, 2),
           7: (2, 0),
           8: (2, 1),
           9: (2, 2),
           0: (3, 1),
           '*': (3, 0),
           '#': (3, 2)
           }
    curr_l = '*'
    curr_r = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            curr_l = i
        elif i in right:
            answer += 'R'
            curr_r = i
        else:
            sum_l, sum_r = 0, 0
            for a, b in zip(key[i], key[curr_l]):
                sum_l += abs(a - b)
            for a, b in zip(key[i], key[curr_r]):
                sum_r += abs(a - b)
            if sum_l < sum_r:
                answer += 'L'
                curr_l = i
            elif sum_l > sum_r:
                answer += 'R'
                curr_r = i
            else:
                if hand == "L":
                    curr_l = i
                else:
                    curr_r = i
                answer += hand

    return answer
