
num, max = map(int, input().split())
N = list(map(int, input().split()))
min = 999999
for i in range(len(N)-2):
    for j in range(i+1,len(N)-1):
        for k in range(j + 1, len(N)):
            sum = N[i] + N[j] + N[k]
            diff = max - sum
            if diff < 0:
                continue
            if min >= diff:
                min = diff
                final_sum = sum
print(final_sum)


