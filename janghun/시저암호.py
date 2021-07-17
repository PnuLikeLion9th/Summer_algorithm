def solution(s, n):
    alphabets=[]
    stirnglen=len(s)
    for alphabet in range(0,len(s)):
        alphabets.append(s[alphabet])

    print(alphabets)

    for i in range(0,len(alphabets)):
        code=ord(alphabets[i])
        pluscode = code + n
        if code >=65 and code <=90:
            if pluscode >90 :
                lastcode = pluscode-26
                alphabets[i]=chr(lastcode)
            else :
                alphabets[i]=chr(pluscode)
        if code>=97 and code <=122:
            if pluscode >122:
                lastcode = pluscode-26
                alphabets[i]=chr(lastcode)
            else :
                alphabets[i]=chr(pluscode)

    answer=''.join(alphabets)
    return(answer)