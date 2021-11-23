import math 
  
def printWalk(A, B, C, D):
    n = 1
    s = ""
    for i in range(100):
        k =0
        if n&A > 0:
            s += "E"
            A = A-n
            k+=1
        if n&B > 0:
            s += "W"
            B = B-n
            k+=1
        if n&C > 0:
            s += "N"
            C = C-n
            k+=1
        if n&D > 0:
            s += "S"
            D = D-n
            k+=1
        
        if k!=1:
            return False, ""

        if A+B+C+D<=0:
            break
        n = n << 1
    return True, s

def sol(X, Y):
    A, B, C, D = 0, 0, 0, 0
    
    minS = None
    # for A in range(100):
    #     for C in range(100):
    for W in range(500):
        for A in range(W+1):
            C = W-A

            # print(A, C)
            # input()
            B = A-(X)
            D = C-(Y)

            if B <0 or D <0:
                continue
            
            flag = True
            for px, py in [(A, B), (A, C), (A, D), (B, C), (B, D), (C, D)]:
                if px&py >0:
                    flag=False
                    break

            if not flag:
                continue

            if A&B&C&D>0:
                continue

            n = A|B|C|D
            p = math.log2(n+1)
            # if A==2 and C==4:
            #     print(A, B, C, D)
            #     print(A&B&C&D)
            #     print((A|B|C|D))
            #     print(p, int(p), n)

            
            # if ~n==0:
            if p!=int(p):
                continue
            
            done, s = printWalk(A, B, C, D)
            if done:
                return s
                # if minS is None:
                #     minS = s

                # if len(minS) > len(s):
                #     minS = s
            # logp = math.log2(p)
            # if int(logp)==logp:
            #     print("YEAH")
    if minS is None:
        return "IMPOSSIBLE"
    else:
        return minS

# T = int(input())
# for i in range(T):
#   X, Y = [int(n) for n in input().split()]
#   S = sol(X, Y)
#   print("Case #{}: {}".format(i+1, S))

for x in range(10, 20):
    for y in range(10, 20):
        if sol(x, y)=="IMPOSSIBLE":
            print(x, y)
            # break
        # input()
# print(sol(-2, -3))
# print(sol(3, 0))
# print(sol(-1, -1))
