def findPermutation(n, p, q):
    r=[p.index(q[i])+1 for i in range(n)]
    return r