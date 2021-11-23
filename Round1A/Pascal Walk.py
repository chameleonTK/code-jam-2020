def getTriangle(arr):
    if arr is None:
        return [(1, set([1]))]
    elif len(arr)==1:
        return [(1, set([2, 3])), (1, set([2]))]

    newarr = [(1, set())]
    for i in range(len(arr)-1):
        rn, _ = arr[i]
        rn_1, _ = arr[i+1]
        n = rn + rn_1
        newarr.append((n, set()))
    newarr.append((1, set([len(newarr)+1])))


    for i in range(len(newarr)-2, -1, -1):
        n, s = newarr[i]
        #left
        nl, sl = newarr[i+1]
        for k in sl:
            s.add(k+n)
        
        #up
        nu, su = arr[i]
        for k in su:
            s.add(k+n)

    return newarr

def backtrack(N, p, triangle):
    i, j = p
    out = [p]
    while True:
        n, _ = triangle[i][j]
        N -= n

        if N==0:
            break
        if i==0 and j==0:
            break

        error = True
        if j+1 < len(triangle[i]):
            #left 
            nl, sl = triangle[i][j+1]
            if N in sl:
                i, j = i, j+1
                out.append((i, j))
                continue

        if i-1 >= 0:
            #up 
            if j==len(triangle[i])-1:
                nu, su = triangle[i-1][j-1]
            else:
                nu, su = triangle[i-1][j]

            if N in su:
                if j==len(triangle[i])-1:
                    i, j = i-1, j-1
                else: 
                    i, j = i-1, j
                out.append((i, j))
                continue
        
        if error:
            print("ERROR")
            break

    return out

p = getTriangle(None)
triangle = [p]

def sol(N):
    global triangle

    p = triangle[0]
    idx = 0
    for i in range(1000):
        for j in range(len(p)):
            (n, s) = p[j]
            if N in s:
                return backtrack(N, (i, j), triangle)

        idx += 1
        if idx < len(triangle):
            p = triangle[idx]
        else:
            p = getTriangle(p)
            triangle.append(p)
        
        print(triangle)

    return [(1,1)]

T = int(input())
for i in range(T):
  N = int(input())
  P = sol(N)
  print("Case #{}:".format(i+1))
  for x, y in P[::-1]:
      print(x+1, y+1)