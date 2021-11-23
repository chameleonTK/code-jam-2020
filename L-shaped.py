def verticalLines(mat):

    lines = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==0:
                continue

            l = 1
            for k in range(i+1, len(mat)):
                l += 1
                if mat[k][j]==0:
                    break

                # if l < 4:
                #     continue

                if l%2==0:
                    # print((i,j,k), l)
                    lines.append((i, j, k))
    return lines

def findLShape(mat):
    cnt = 0
    lines = verticalLines(mat)
    for i, j, k in lines:
        # print("XXX", i,j,k)
        _cnt = 0
        l = (k-i)+1

        ep = int(l/2)
        if ep==1:
            ep = -1

        
        # horizontal line at the end
        c = 0
        for p in range(j, -1, -1):
            if mat[k][p]==0:
                break
            c += 1

            # if i==1 and j==3 and k==2:
            #     print("WWWW", p)
            if c==ep or c==l*2:
                _cnt += 1
        

        c = 0
        for p in range(j, len(mat[0])):
            if mat[k][p]==0:
                break
            c += 1
            if c==ep or c==l*2:
                _cnt += 1
        

        # horizontal line at the top
        c = 0
        for p in range(j, -1, -1):
            if mat[i][p]==0:
                break
            c += 1
            if c==ep or c==l*2:
                _cnt += 1
        

        c = 0
        for p in range(j, len(mat[0])):
            if mat[i][p]==0:
                break
            c += 1
            if c==ep or c==l*2:
                _cnt += 1
        
        
        cnt += _cnt
        # print((i+1, j+1, k+1), _cnt)
    return cnt

T = int(input())
for t in range(T):
    R, C = [int(i) for i in input().strip().split()]

    mat = []
    for i in range(R):
        s = [int(i) for i in input().strip().split()]
        
        mat.append(s)
    
    o = findLShape(mat);
    print(f"Case #{t+1}:", o)


# Each of the segments must be a "good" segment.
# The two segments must be perpendicular to each other.
# The segments must share one cell that is an endpoint of both segments.
# Segments must have length at least 2.
# The length of the longer segment is twice the length of the shorter segment.