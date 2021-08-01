def solution(answers):
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*1250
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    aa=a[0:len(answers)]
    bb=b[0:len(answers)]
    cc=c[0:len(answers)]
    def score(test,sol):
        count=0
        for i in range(len(sol)):
            if test[i] == sol[i]: count+=1
        return count
    max_score= max(score(aa,answers),score(bb,answers),score(cc,answers))
    k=[score(aa,answers),score(bb,answers),score(cc,answers)]
    j=[]
    for i in range(3):
        if max_score == k[i]:
            j.append(i+1)
    return j