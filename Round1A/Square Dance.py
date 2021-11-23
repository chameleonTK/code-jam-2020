def interest_level(S):
    cc = 0
    for row in S:
        cc += sum(row)
    return cc

def get_neibours(R, C, S, i, j):
    
    neibours = []
    #left
    for py in range(j+1, C):
        if S[i][py]!=0:
            neibours.append(S[i][py])
            break

    for py in range(j-1, -1, -1):
        if S[i][py]!=0:
            neibours.append(S[i][py])
            break

    for px in range(i+1, R):
        if S[px][j]!=0:
            neibours.append(S[px][j])
            break

    for px in range(i-1, -1, -1):
        if S[px][j]!=0:
            neibours.append(S[px][j])
            break

    return neibours

def sol(R, C, S):

    intlevel = interest_level(S)
    while True:

        cc = 0
        eliminate = []
        for i in range(R):
            for j in range(C):
                if S[i][j] > 0:

                    neibours = get_neibours(R, C, S, i, j)
                    if len(neibours)==0:
                        cc += 1
                        continue

                    avg_score = sum(neibours)/len(neibours)
                    if avg_score > S[i][j]:
                        eliminate.append((i, j))
                else:
                    cc += 1

        if len(eliminate)==0:
            break

        for (i, j) in eliminate:
            S[i][j] = 0
        
        intlevel += interest_level(S)
    
    return intlevel
    
T = int(input())
for t in range(T):
    R, C = [int(n) for n in input().split()]

    S = []
    for i in range(R):
        s = [int(n) for n in input().split()]
        S.append(s)

    N = sol(R, C, S)
    print("Case #{}: {}".format(t+1, N))

# p = [
#     [1,1,1],
#     [1,2,1],
#     [1,1,1],
# ]

# print(sol(3, 3, p))