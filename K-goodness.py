# input()
# N = 20
# for i in range(1, N/2+1):
#     print(i, N-i+1)

# import math
T = int(input())
for t in range(T):
    N, K = [int(i) for i in input().strip().split()]
    s = input()
    r = s[::-1]
    
    goodness = 0

    l = int(len(r)/2)
    if len(r)%2!=0:
        l = int(len(r)/2)

    for i in range(l):
        if s[i]!=r[i]:
            goodness += 1

    # print("AAA",goodness, K)
    o = abs(goodness - K)
    print(f"Case #{t+1}:", o)
    