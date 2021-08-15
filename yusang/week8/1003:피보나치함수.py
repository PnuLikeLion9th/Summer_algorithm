# resultZero = []
# resultOne = []



# def fibonacci(n) : 
#     if(n == 0) : 
#         resultZero.append(0) 
#         return 0;
#     elif n == 1 :
#         resultOne.append(0)
#         return 1;
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input())

# for _ in range(n):
#     i = int(input())
#     fibonacci(i)
#     print(len(resultZero) + " " + len(resultOne))
#     resultZero = []
#     resultOne = []


a = int(input())
 
zero = [1,0,1]
one = [0,1,1]
 
def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))
 
for i in range(a):
    k = int(input())
    cal(k)
