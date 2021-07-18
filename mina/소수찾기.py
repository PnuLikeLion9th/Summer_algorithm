#소수찾기이이이

#일단 에라토스테네스의 체 먼저 찾아봄 

def prime_list(n):
    sieve=[True]*n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

#풀이풀이

def solution(n):
    num = set(range(2,n+1)) #2~에서 n+1까지
    
    for i in range(2,n+1): #반복반복 
        if i in num: 
            num -= set(range(2*i, n+1, i)) #i가 num 안에 있으면 나가리
 
    return len(num) #num에 있는 i 개수!! len은 리스트에 있는 원소 개수 알랴쥼
