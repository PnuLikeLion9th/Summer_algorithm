# 백준_1107_리모컨_브루트포스_골드 5

n = int(input())
m = int(input())

remote = [str(i) for i in range(10)]
if m != 0:
    for num in list(input().split()):
        remote.remove(str(num))

result = abs(n-100)
for num in range(n+500001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in remote:
            break
        if i == len(num) - 1:
            result = min(result, abs(n-int(num)) + len(str(num)))

print(result)
