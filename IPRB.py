k_in = int(input("k: "))
m_in = int(input("m: "))
n_in = int(input("n: "))

def computeProbability(k,m,n, dom, tot):
    print(k,m,n)
    if k == 0 and m == 0 and n == 0:
        return dom, tot
    if k > 0:
        dom += (k-1 + m + n)*4
        tot += (k-1 + m + n)*4
        return computeProbability(k-1, m, n, dom, tot)
    elif m > 0:
        dom += (m-1)*3 + n*2
        tot += (m-1 + n)*4        
        return computeProbability(0, m-1, n, dom, tot)
    else:        
        tot += (n-1)*4              
        return computeProbability(0, 0, n-1, dom, tot)

dominantInds,totalPossibleInds = computeProbability(k_in,m_in,n_in, 0, 0)

print(dominantInds/totalPossibleInds)