# 백준_1759_암호 만들기_백트래킹_골드 5
# N과 M 시리즈를 다 풀었다면, 조합을 만드는 과정에서 조건을 몇 개 추가하여 간단히 풀수있다

def solve(index, depth, cnt1, cnt2):  # 중복되는 것은 없다는 조건때문에 매개변수 index 사용, cnt1은 모음의 갯수, cnt2는 자음의 갯수이다
    if depth == l and cnt1 >= 1 and cnt2 >= 2:  # 문제에서 주어진 모든 조건들을 만족했을때 암호를 출력한다
        for i in result:
            print(i, end='')
        print()
        return

    for i in range(index, c):
        result.append(lst[i])
        if lst[i] in alpha:  # lst[i]가 모음 일때
            solve(i+1, depth+1, cnt1+1, cnt2)
        else:  # lst[i]가 자음 일떄
            solve(i+1, depth+1, cnt1, cnt2+1)
        result.pop()


l, c = map(int, input().split())
lst = sorted(list(input().split()))
alpha = ['a', 'e', 'i', 'o', 'u']  # 모음을 담은 list
result = []
solve(0, 0, 0, 0)
