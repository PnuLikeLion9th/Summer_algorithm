t = int(input())
for i in range(t):
    n = int(input())
    z = [1,0,1]
    o = [0,1,1]
    if n>=3:
        for j in range(3,t+1):
            z.append(z[j-1]+z[j-2])
            o.append(o[j-1]+o[j-2])
    print(z[n],o[n])
