def solution(s):
    s = s.lower()
    words = s.split(' ')
    answer = ''
    for word in words:
        for idx, letter in enumerate(word):
            if idx % 2 == 0:
                answer += letter.upper()
            else:
                answer += letter
        answer += ' '
    return answer
