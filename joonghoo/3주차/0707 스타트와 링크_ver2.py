# 백준_14889_스타트와 링크_백트래킹_실버 3
# combinations 함수를 이용하여 조합을 구해서 풀이 진행
# i의 대칭되는 index가 -i-1임을 이용하면 간단하게 코드를 짤 수 있다

import sys
import itertools
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
nums = [i for i in range(n)]
possible_team = []

# n//2 길이의 각각의 조합을 possible_team 리스트에 추가한다
for team in list(itertools.combinations(nums, n//2)):
    possible_team.append(team)

result = sys.maxsize
for i in range(len(possible_team)//2):

    team = possible_team[i]  # start팀의 구성원을 team에 대입
    sum_start = 0
    for j in range(n//2):  # start팀의 능력치를 계산하는 반복문
        for k in range(n//2):
            sum_start += lst[team[j]][team[k]]

    # list에서 i의 대칭값은 -i-1임을 이용하여 link팀의 구성원을 team에 대입함
    team = possible_team[-i-1]
    sum_link = 0
    for j in range(n//2):  # link팀의 능력치를 계산하는 반복문
        for k in range(n//2):
            sum_link += lst[team[j]][team[k]]

    result = min(result, abs(sum_start-sum_link))  # 차이의 최솟값을 구해준다

print(result)
