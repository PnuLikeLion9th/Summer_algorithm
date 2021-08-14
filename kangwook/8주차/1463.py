a,b,c = map(int,input().split())
if c==b: print(-1)
else:
    i=a/(c-b)
    if i < 0: print(-1)
    else: print(int(i)+1)
    