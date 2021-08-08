n = int(input())
lst = list(map(int, input().split()))
lst.sort()

lt, rt = 0, n-1  # 투포인터 탐색을 위한 left(처음부터), right(끝부터)
answer_lt, answer_rt = lt, rt
answer = lst[lt]+lst[rt]

while lt < rt:
    tmp = lst[lt]+lst[rt]
    if abs(tmp) < abs(answer):
        answer = tmp
        answer_lt = lt
        answer_rt = rt
        if answer == 0:
            break

    if tmp < 0:
        lt += 1
    else:
        rt -= 1

print(lst[answer_lt], lst[answer_rt])
