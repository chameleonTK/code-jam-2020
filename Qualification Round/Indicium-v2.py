 
def create_matrix(N):
    mat = []

    for i in range(N):
        row = []
        for n in range(1, N-i+1):
            row.append(n)
        
        lst = list(range(N-i+1, N+1))
        lst.reverse()
        for n in lst:
            row.insert(0, n)
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        print(" ".join([str(r) for r in row]))

def get_trace(mat):
    t = 0
    for i in range(len(mat)):
        t += mat[i][i]
    return t

def swap_col(N, mat, col1, col2):
    newmat = []
    for i in range(N):
        newmat.append([m for m in mat[i]])

    tmp = []
    for i in range(N):
        tmp.append(mat[i][col1])
    
    for i in range(N):
        mat[i][col1] = mat[i][col2]
        mat[i][col2] = tmp[i]
    
    return mat

def swap_row(N, mat, row1, row2):
    newmat = []
    for i in range(N):
        newmat.append([m for m in mat[i]])

    tmp = []
    for i in range(N):
        tmp.append(mat[row1][i])
    
    for i in range(N):
        mat[row1][i] = mat[row2][i]
        mat[row2][i] = tmp[i]
    
    return mat

# all_traces = set()
from random import randint
import random
def sol(N, K):
    # global all_traces
    random.seed(0)
    mat = create_matrix(N)
    if K==N:
        return "POSSIBLE", mat

    for i in range(100):
        mat = swap_col(N, mat, randint(0, N-1), randint(0, N-1))
        mat = swap_row(N, mat, randint(0, N-1), randint(0, N-1))

        trace = get_trace(mat)
        for col1 in range(N):
            for col2 in range(col1+1, N):
                newtrace = trace
                newtrace -= (mat[col1][col1] + mat[col2][col2])
                newtrace += (mat[col1][col2] + mat[col2][col1])
                # print("-", mat[col1][col1], mat[col2][col2])
                # print("+", mat[col1][col2], mat[col2][col1])
                # print(trace)
                # all_traces.add(newtrace)
                if newtrace == K:
                    return "POSSIBLE", swap_col(N, mat, col1, col2)
            
    return "IMPOSSIBLE", None

# all_traces = set()
# sol(, 1)
# print(all_traces)

ans = {"2": {"2": ["POSSIBLE", [[1, 2], [2, 1]]], "3": ["IMPOSSIBLE", None], "4": ["POSSIBLE", [[2, 1], [1, 2]]]}, "3": {"3": ["POSSIBLE", [[1, 2, 3], [3, 1, 2], [2, 3, 1]]], "4": ["IMPOSSIBLE", None], "5": ["IMPOSSIBLE", None], "6": ["POSSIBLE", [[1, 2, 3], [2, 3, 1], [3, 1, 2]]], "7": ["IMPOSSIBLE", None], "8": ["IMPOSSIBLE", None], "9": ["POSSIBLE", [[3, 1, 2], [2, 3, 1], [1, 2, 3]]]}, "4": {"4": ["POSSIBLE", [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]]], "5": ["IMPOSSIBLE", None], "6": ["POSSIBLE", [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 2, 1], [4, 3, 1, 2]]], "7": ["POSSIBLE", [[1, 2, 3, 4], [3, 1, 4, 2], [4, 3, 2, 1], [2, 4, 1, 3]]], "8": ["POSSIBLE", [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]], "9": ["POSSIBLE", [[1, 2, 3, 4], [2, 4, 1, 3], [4, 3, 2, 1], [3, 1, 4, 2]]], "10": ["POSSIBLE", [[1, 2, 3, 4], [2, 4, 1, 3], [3, 1, 4, 2], [4, 3, 2, 1]]], "11": ["POSSIBLE", [[1, 2, 3, 4], [3, 4, 2, 1], [2, 1, 4, 3], [4, 3, 1, 2]]], "12": ["POSSIBLE", [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]]], "13": ["POSSIBLE", [[2, 1, 3, 4], [3, 4, 2, 1], [1, 3, 4, 2], [4, 2, 1, 3]]], "14": ["POSSIBLE", [[3, 1, 2, 4], [1, 4, 3, 2], [2, 3, 4, 1], [4, 2, 1, 3]]], "15": ["IMPOSSIBLE", None], "16": ["POSSIBLE", [[4, 1, 2, 3], [1, 4, 3, 2], [2, 3, 4, 1], [3, 2, 1, 4]]]}, "5": {"5": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [3, 5, 1, 2, 4], [4, 3, 5, 1, 2], [5, 4, 2, 3, 1]]], "6": ["IMPOSSIBLE", None], "7": ["POSSIBLE", [[1, 2, 3, 4, 5], [3, 1, 4, 5, 2], [4, 5, 2, 1, 3], [5, 3, 1, 2, 4], [2, 4, 5, 3, 1]]], "8": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [3, 5, 1, 2, 4], [5, 4, 2, 3, 1], [4, 3, 5, 1, 2]]], "9": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [4, 5, 1, 3, 2], [3, 4, 5, 2, 1], [5, 3, 2, 1, 4]]], "10": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [3, 4, 5, 1, 2], [5, 3, 1, 2, 4], [4, 5, 2, 3, 1]]], "11": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 3, 1, 5, 4], [3, 5, 4, 1, 2], [4, 1, 5, 2, 3], [5, 4, 2, 3, 1]]], "12": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 3, 1, 5, 4], [3, 4, 5, 1, 2], [5, 1, 4, 2, 3], [4, 5, 2, 3, 1]]], "13": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 3, 1, 5, 4], [5, 1, 4, 2, 3], [4, 5, 2, 3, 1], [3, 4, 5, 1, 2]]], "14": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 1, 4, 5, 3], [3, 4, 5, 1, 2], [4, 5, 2, 3, 1], [5, 3, 1, 2, 4]]], "15": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 3, 1, 5, 4], [3, 4, 5, 1, 2], [4, 5, 2, 3, 1], [5, 1, 4, 2, 3]]], "16": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [4, 1, 5, 2, 3], [5, 4, 1, 3, 2], [3, 5, 2, 1, 4]]], "17": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 4, 1, 5, 3], [4, 3, 5, 2, 1], [5, 1, 4, 3, 2], [3, 5, 2, 1, 4]]], "18": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 4, 5, 1, 3], [3, 5, 4, 2, 1], [4, 3, 1, 5, 2], [5, 1, 2, 3, 4]]], "19": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 5, 1, 3, 4], [3, 4, 5, 1, 2], [4, 3, 2, 5, 1], [5, 1, 4, 2, 3]]], "20": ["POSSIBLE", [[1, 2, 3, 4, 5], [2, 5, 4, 1, 3], [3, 4, 5, 2, 1], [4, 3, 1, 5, 2], [5, 1, 2, 3, 4]]], "21": ["POSSIBLE", [[2, 1, 3, 4, 5], [1, 5, 4, 2, 3], [3, 4, 5, 1, 2], [4, 3, 2, 5, 1], [5, 2, 1, 3, 4]]], "22": ["POSSIBLE", [[3, 1, 2, 4, 5], [1, 5, 4, 2, 3], [2, 4, 5, 3, 1], [4, 3, 1, 5, 2], [5, 2, 3, 1, 4]]], "23": ["POSSIBLE", [[4, 1, 2, 3, 5], [1, 5, 3, 4, 2], [2, 4, 5, 1, 3], [3, 2, 4, 5, 1], [5, 3, 1, 2, 4]]], "24": ["IMPOSSIBLE", None], "25": ["POSSIBLE", [[5, 1, 2, 3, 4], [1, 5, 3, 4, 2], [2, 4, 5, 1, 3], [3, 2, 4, 5, 1], [4, 3, 1, 2, 5]]]}}

def sol2(N, K):
    return ans[str(N)][str(K)]


T = int(input())
for t in range(T):
    N, K = [int(n) for n in input().split()]
    
    if N<=5:
        message, matrix = sol2(N, K)
    else:
        message, matrix = sol(N, K)
        
    print("Case #{}: {}".format(t+1, message))
    if message != "IMPOSSIBLE":
        print_matrix(matrix)

# print(sol(3, 6))
# print(sol(2, 2))
# print(sol(2, 3))
# print(sol(2, 4))