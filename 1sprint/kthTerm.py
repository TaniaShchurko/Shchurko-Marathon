def kthTerm(n, k):
    num=[]
    degrees=[n**i for i in range(10)]
    for i in range(10):
        num.append(n**i)
        for j in range(num.index(degrees[i])):
            num.append(degrees[i]+num[j])
    return num[k-1]