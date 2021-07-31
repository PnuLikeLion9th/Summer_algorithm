n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = list(range(1, n + 1))
ret = 0

for target in arr:
    idx = q.index(target)
    if len(q) // 2 >= idx:
        ret += idx
    else:
        ret += len(q) - idx
    q = q[idx + 1:] + q[:idx]
print(ret)