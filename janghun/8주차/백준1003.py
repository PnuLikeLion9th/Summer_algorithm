sum0=[1,0,1]
sum1=[0,1,1]
a=int(input())

def fibonacci(n) :
    if len(sum0) <= n :
        for i in range(len(sum0), n+1) :
            sum0.append(sum0[i-1]+sum0[i-2])
            sum1.append(sum1[i-1]+sum1[i-2])
    print(sum0[n],sum1[n])

for i in range(a):
    N = int(input())
    fibonacci(N)