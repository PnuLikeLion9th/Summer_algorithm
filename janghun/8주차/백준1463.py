a = int(input())

n = [0,0,1,1]

for i in range(4, a+1):
    n.append(n[i-1]+1)
    if i%2 == 0:
        n[i] = min(n[i//2]+1, n[i])
    if i%3 == 0:
        n[i] = min(n[i//3]+1, n[i])

print(n[a])