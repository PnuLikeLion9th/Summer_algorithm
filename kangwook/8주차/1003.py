t=int(input())
a=[int(input())for _ in range(t)]

def f(n):
    if n == 1 : 
        return 0
    elif n == 2 : return 1
    fib_array = [0,1]
    for i in range(2,n+1):
        num = fib_array[i-1]+fib_array[i-2]
        fib_array.append(num)
    return fib_array[n-1]

for k in a:
    print(f(k),f(k+1))