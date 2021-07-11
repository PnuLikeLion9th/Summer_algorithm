def solution(s):
    sentence = s.lower().split(" ")

    for i in range(len(sentence)):
        word = list(sentence[i])
        for j in range(len(word)):
            if j % 2 == 0:
                word[j] = word[j].upper()
        sentence[i] = ''.join(word)

    return ' '.join(sentence)


print(solution("try hello world"))


# 짝수번째 알파벳 => 대문자
# 홀수번째 알파벳 => 소문자
