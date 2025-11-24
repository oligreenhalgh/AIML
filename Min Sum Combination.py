import argminsum

x = [32,31,30,20,21,4,3,2,1]
M = 2

def minsumcomb(x,M):
    N = len(x)
    S = [[0 for side1 in range(M+1)] for side2 in range(N + 1)]
    S[0][0] = argminsum.zero
    for m in range(1,M+1):
        S[0][m] = argminsum.inf
    for n in range(1,N+1):
        S[n][0] = S[n-1][0]
        for m in range(1,M+1):
            t1 = S[n-1][m]
            xn = x[n-1]
            x_formatted = argminsum.argminsum(xn,[xn])
            t2 = S[n-1][m-1] + x_formatted
            S[n][m] = argminsum.min(t1, t2)
    return S


s= minsumcomb(x, M)
print(s)


