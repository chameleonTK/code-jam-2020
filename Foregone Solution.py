def sol(N):
    a = 0
    b = 0

    for i in N:
        # print(i)
        if i=="4":
            a = a*10+2
            b = b*10+2
        else:
            a = a*10+int(i)
            b = b*10
    
    return a, b

T = int(input())
for i in range(T):
  N = input()
  
  a, b = sol(N)
  print("Case #{}: {} {}".format(i, a, b))