def get_diagonal(N, K):
    k = [K//N for i in range(N)]
    rest = K - (K//N)*N
    for i in range(rest):
        k[i] += 1

    return k

def create_matrix(N, K):
    mat = []

    rows = []
    cols = []
    for i in range(N):
        mat.append([0]*N)
        rows.append(set())
        cols.append(set())

    diagnalvals = get_diagonal(N, K)
    for i in range(N):
        mat[i][i] = diagnalvals[i]
        rows[i].add(diagnalvals[i])
        cols[i].add(diagnalvals[i])

    # print(diagnalvals)
    return mat, rows, cols

def print_matrix(mat):
    for row in mat:
        print(" ".join([str(r) for r in row]))
    
def possible_num(loc, choices, rows, cols):
    i, j = loc
    num = choices - rows[i]
    num = num - cols[j]
    return num

debug = False

def get_trace(mat):
    t = 0
    for i in range(len(mat)):
        t += mat[i][i]
    return t

# all_possible_trace = set()
def copy_matrix(mat):
    c = []
    for i in range(len(mat)):
        c.append([m for m in mat[i]])
    return c


target = None
def recur(K, mat, loc, choices, rows, cols):
    global target
    i, j = loc
    # input()
    if i>=len(rows):
        target = copy_matrix(mat)
        return None

    if target is not None:
        return None

    if mat[i][j] != 0:
        num = [mat[i][j]]
    else:
        num = possible_num(loc, choices, rows, cols)

    if len(num)==0:
        return None

    # print("loc", loc, num)
    # print("FROM")
    # print_matrix(mat)
    for n in num:
        mat[i][j] = n

        rows[i].add(n)
        cols[j].add(n)

        # print("TEST", loc, n)
        # print_matrix(mat)
        if j < len(rows)-1:
            recur(K, mat, (i, j+1), choices, rows, cols)
        else:
            recur(K, mat, (i+1, 0), choices, rows, cols)


        if i==j:
            continue
            
        mat[i][j] = 0
        rows[i].remove(n)
        cols[j].remove(n)

        if target is not None:
            return None

def sol(N, K):
    global target
    mat, rows, cols = create_matrix(N, K)
    # print_matrix(mat)

    choices = set(range(1, N+1))
    target = None
    recur(K, mat, (0, 1), choices, rows, cols)
    if target is None:
        return "IMPOSSIBLE", None
    else:
        
        return "POSSIBLE", target
    
# T = int(input())
# for t in range(T):
#     N, K = [int(n) for n in input().split()]
#     message, matrix = sol(N, K)
#     print("Case #{}: {}".format(t+1, message))
#     if message != "IMPOSSIBLE":
#         print_matrix(matrix)

p = {}
for n in range(6, 51):
    p[n] = {}
    for k in range(n, n*n+1):
        p[n][k] = sol(n, k)
        print(n, k)

    import json
    with open("in"+str(n)+".json", 'w') as outfile:
        json.dump(p, outfile)