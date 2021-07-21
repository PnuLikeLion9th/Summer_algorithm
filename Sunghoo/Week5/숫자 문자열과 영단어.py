from collections import deque


def solution(s):
    alphabet = {
        'zero': "0",
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    alphabet = []
    s = deque(s)
    answer = ''
    temp = ''

    while s:
        i = s.popleft()
        if i.isdigit():
            answer += i

        else:
            temp += i
            if temp in alphabet:
                answer += alphabet[temp]
                temp = ''

    return int(''.join(answer))

num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
def solution2(s):
    answer = s
    for key, value in num_dic.items():
        print(answer.replace(key, value))
        # answer = answer.replace(key, value)
    # return int(answer)
s = "2three45sixseven"
print(solution2(s))
