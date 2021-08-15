def f(n):
    if n == 1 : 
        return 0
    elif n == 2 : return 1
    fib_array = [0,1]
    for i in range(2,n+1):
        num = fib_array[i-1]+fib_array[i-2]
        fib_array.append(num)
    return fib_array[n-1]

print(f(7))


# print(f(9))

# t=int(input())
# a=[int(input())for _ in range(t)]
# zero, one=0,0
# def fib(n,zero,one):
#     if n == 0: 
#         zero+=1 
#     elif n == 1: 
#         one +=1 
#     else:
#         fib(n-1,zero,one) 
#         fib(n-2,zero,one)    
#     return print(zero,one)    
# for k in a:
#     fib(k,zero,one)

