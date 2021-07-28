def solution(answers):  # answers 는 정답이 든 배열
    result = [-1]
    whatever = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(3):
        count = 0
        whatever[i] = whatever[i] * ((len(answers) // len(whatever[i])) + 1)

        for j in range(len(answers)):
            if whatever[i][j] == answers[j]:
                count += 1
        result.append(count)

    answer = []
    maxx = max(result)

    for k in range(len(result)):
        if maxx == result[k]:
            answer.append(k)

    return answer
