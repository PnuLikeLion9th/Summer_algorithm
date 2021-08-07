answer = 0


def solution(begin, target, words):
    visited = [0] * len(words)
    dfs(begin, target, words, visited)
    return answer


def dfs(begin, target, words, visited):
    stack = []
    global answer
    if begin == target:
        return answer

    if answer > len(words):
        return 0

    # while 0 in visited:
    for i in range(len(words)):
        if sum([1 for a, b in zip(begin, words[i]) if a != b]) == 1 and visited[i] == 0:
            stack.append(words[i])
            print(stack)

            visited[i] = 1
    while stack:
        be = stack.pop()
        answer += 1
        dfs(be, target, words, visited)

    return 0
