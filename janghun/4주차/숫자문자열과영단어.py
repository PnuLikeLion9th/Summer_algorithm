def solution(s):
    string=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(0,len(string)):
        if string[i] in s:
            s=s.replace(string[i],str(i))
    answer=int(s)
    return(answer)