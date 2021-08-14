N=int(input())

def sums(a):
    if a==1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return sums(a-1)+sums(a-2)+sums(a-3)

for i in range(N):
    a = int(input())
    print(sums(a))