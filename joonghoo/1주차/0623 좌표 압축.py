# 백준18870_좌표 압축_정렬_실버 2

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

sort_nums = sorted(list(set(nums)))
lank = []

for i in range(len(sort_nums)):
    lank.append([sort_nums[i], i])

lank = dict(lank)

for num in nums:
    print(lank[num], end=' ')
