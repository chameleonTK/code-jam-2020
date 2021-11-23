import copy
def resolve(A):
    A = copy.copy(A)
    N = len(A)
    fixable = True
    cnt = 0

    while(fixable):
        fixable = False
        # print(A)
        for i in range(N):
            error = 0
            x, y = 0, 0
            for j in range(N):
                if A[i][j]==-1:
                    error += 1
                    x, y = i, j
            
            if error == 1:
                A[x][y] = True
                fixable = True
            
            error = 0
            x, y = 0, 0
            for j in range(N):
                if A[j][i]==-1:
                    error += 1
                    x, y = j, i
            if error == 1:
                A[x][y] = True
                fixable = True

        
        c = 0
        needfix = False
        for i in range(N):
            for j in range(N):
                if A[i][j]==-1:
                    needfix = True
                    c += 1
        
        # print("CNT", cnt, c)
        if cnt == c:
            break
        
        cnt = c
    return A

def calcost(A, B):
    N = len(A)
    cost = 0
    for i in range(N):
        for j in range(N):
            if A[i][j]==-1:
                cost += B[i][j]
    return cost

def cccccc(mat):
    A = []
    N = len(mat)
    for i in range(N):
        r = []
        for j in range(N):
            r.append(mat[i][j])
        A.append(r)
    return A
                

def findChecksum(A, B, R, C):
    A = resolve(A)
    
    q = []
    cc = {}
    N = len(A)
    for i in range(N):
        for j in range(N):
            if A[i][j]==-1:
                q.append((i,j))
    
    if len(q)==0:
        return 0

    # print("=================")
    # print(A)
    for i, j in q:
        A[i][j] = True
        
        NewA = resolve(cccccc(A))
        
        for x in range(N):
            for y in range(N):
                if A[x][y]!=NewA[x][y]:
                    q.remove((x, y))
        
        cc[(i, j)] = calcost(NewA, B)+B[i][j]
    
        A[i][j] = -1

    # print(cc)
    mincost = cc[list(cc.keys())[0]]
    for k in cc:
        mincost = min(mincost, cc[k])

    return mincost

T = int(input())
for t in range(T):
    N = int(input())
    matA = []
    for i in range(N):
        s = [int(i) for i in input().strip().split()]
        
        matA.append(s)
    
    matB = []
    for i in range(N):
        s = [int(i) for i in input().strip().split()]
        
        matB.append(s)
    
    R = [int(i) for i in input().strip().split()]
    C = [int(i) for i in input().strip().split()]
    
    o = findChecksum(matA, matB, R, C);
    print(f"Case #{t+1}:", o)