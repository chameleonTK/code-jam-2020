 
def create_matrix(N):
    mat = []

    rows = []
    cols = []
    for i in range(N):
        mat.append([0]*N)
        rows.append(set())
        cols.append(set())

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

latin_sq = None
def recur(K, mat, loc, choices, rows, cols):
    global latin_sq
    i, j = loc
    if debug:
        input()

    if latin_sq is not None:
        return None

    if i>=len(rows):
        trace = get_trace(mat)
        
        if trace==K:
            latin_sq = copy_matrix(mat)
        return None

    num = possible_num(loc, choices, rows, cols)
    if len(num)==0:
        if debug:
            print("- stop -")
        return None

    for n in num:
        mat[i][j] = n
        if debug:
            print("call", loc, "put", n)
            print_matrix(mat)
            print("NEXT")

        rows[i].add(n)
        cols[j].add(n)

        if j < len(rows)-1:
            recur(K, mat, (i, j+1), choices, rows, cols)
        else:
            recur(K, mat, (i+1, 0), choices, rows, cols)

        mat[i][j] = 0
        rows[i].remove(n)
        cols[j].remove(n)
        
        if debug:
            print("BACK")
            print_matrix(mat)


def sol(N, K):
    global latin_sq
    mat, rows, cols = create_matrix(N)
    if debug:
        print_matrix(mat)

    choices = set(range(1, N+1))
    latin_sq = None
    recur(K, mat, (0, 0), choices, rows, cols)
    # print_matrix(latin_sq)
    # print("WW", latin_sq)
    if latin_sq is None:
        return "IMPOSSIBLE", None
    else:
        
        return "POSSIBLE", latin_sq
    
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
#     latin_sq = None
# print(sol(2, 2))
# print(sol(2, 3))
# print(sol(2, 4))