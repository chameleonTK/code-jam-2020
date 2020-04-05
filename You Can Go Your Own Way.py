def sol(P, N):
    E = P-1
    S = P-1

    p1 = (0, 0)
    p2 = (0, 0)

    out = ""
    for n in N:
        # print(n)
        if n=="E":
            # nextp2 = (p2[0], p2[1]+1)
            out +="S"
        else:
            # nextp2 = (p2[0]+1, p2[1])
            out +="E"

        # p2 = nextp2
        # print(p2, nextp2)
    return out

# T = int(input())
# for i in range(T):
#   N = input()
  
#   a, b = sol(N)
#   print("Case #{}: {} {}".format(i+1, a, b))

# print(sol(2, "ES"))
# print(sol(5, "EESSSESE"))