n=int(input())
arr=[1,2,3]
if n <=3: print(n)
else:
    for i in range(3,n): #3~n-1
        num=arr[i-1]+arr[i-2]
        arr.append(num)
    print(arr[n-1]%10007)
    