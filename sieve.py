def sieve(n):
    L = [0,0] + [n for n in range(2,n+1)]
    for i in range(n//2):
        if L[i]: 
            for k in range(2*i, n+1, i):
                L[k] = 0
    return [i for i in L if i]
    


