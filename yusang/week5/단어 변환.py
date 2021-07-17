from collections import deque

# 한글자만 다른지 확인


def check(s, begin):
    check = 0
    answer = 0
    for i in range(len(s)):
        if list(s)[i] not in list(begin):

            answer = i
            check += 1
        if check > 1:
            return -1
    if check == 1:
        return answer
    else:
        return -1


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()

    for e in words:
        i = check(e, begin)
        if i != -1:
            temp = list(begin)
            temp[i] = list(e)[i]
            queue.append([''.join(temp), [e]])

    while queue:
        w, location = queue.popleft()
        for e in words:
            if e not in location:
                i = check(e, w)
                if i != -1:
                    temp = list(w)
                    temp[i] = list(e)[i]
                    location.append(e)
                    queue.append([''.join(temp), location])
                    if target == w:
                        return len(location)

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
