import numpy as np
n = 20
k = 100

# optimal distribution in 1-pirate case
init = [k,-1]

def getOptimal(L, ifnormal, K):
    tot = K
    votes = 1
    req = int(np.ceil(((len(L)+1)/2))) if ifnormal else (int(np.floor((len(L)+1)/2))+1)
    m_l = [(L[i],i) for i in range(len(L))]
    m_l.sort(key=lambda x : x[0])
    res_l = list(np.zeros(len(L)+1))
    num = 0
    print(req)
    for (a,b) in m_l:
        if votes >= req:
            break
        res_l[b] = a+1
        votes += 1
        num += (a+1)
    res_l[-1] = tot - num
    return res_l

for i in range(n):
    init = getOptimal(init,False,k)
    print(len(init),init)

