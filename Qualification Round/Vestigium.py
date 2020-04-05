 
def sol(M, mat):
    
    trace = 0
    nrow = 0
    ncol = 0
    for i in range(N):
        trace += mat[i][i]

    for i in range(N):
        d = set()
        for j in range(N):
            d.add(mat[i][j])
        if len(d) < N:
            nrow += 1

    for i in range(N):
        d = set()
        for j in range(N):
            d.add(mat[j][i])
        if len(d) < N:
            ncol += 1
        
    return trace, nrow, ncol

T = int(input())
for t in range(T):
  N = int(input())
  
  mat = []
  for i in range(N):
    m = [int(n) for n in input().split()]
    mat.append(m)

  trace, nrow, ncol = sol(N, mat)
  print("Case #{}: {} {} {}".format(t+1, trace, nrow, ncol))

  