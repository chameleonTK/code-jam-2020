 
def sol(S):
    parens = ""

    level = 0
    for s in S:  
        n = int(s)
        if n == level:
            parens += s
        elif n > level:
            parens += ("("*(n-level))+s
        else:
            parens += (")"*(level-n))+s
        level = n
    
    if level > 0:
        parens += (")"*(level))

    return parens
    
T = int(input())
for t in range(T):
  S = (input())
  parens = sol(S)
  print("Case #{}: {}".format(t+1, parens))


# print(sol("000"))
# print(sol("101"))
# print(sol("111000"))
# print(sol("1"))
# print(sol("021"))
# print(sol("312"))
# print(sol("321"))
# print(sol("4"))
# print(sol("221"))

  