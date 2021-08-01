n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True) #a배열은 내림차순
sorted_b = sorted(b_list) #b배열은 오름차순

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)