import math 
  
def sol(N):
    out = ""
    arr = []

    primes = []
    for i in range(len(N)):
        if N[i] == N[i+1]:
            continue
        
        gcd = int(math.gcd(N[i], N[i+1]))
        # print(i, gcd, N[i], N[i+1])
        
        p1 = N[i]//gcd
        p2 = gcd
        p3 = N[i+1]//gcd

        primes.append(p1)
        primes.append(p2)
        primes.append(p3)

        #backward
        p = p1
        for j in range(i-1, -1, -1):
            newprime = N[j]//p
            primes.insert(0, newprime)
            p = newprime
        

        #forward
        p = p3
        
        # print("START", i+2, N[i+2])
        for j in range(i+2, len(N)):
            # print(N[j], p, N[j]//p)
            newprime = N[j]//p
            primes.append(newprime)
            p = newprime
        
        # print(primes)
        # input()
        break

    
    

    dct = {}
    for p in primes:
        dct[int(p)] = 1

        
    sortedlst = list(dct.keys())
    sortedlst.sort()

    mapkey = {}
    for i, p in enumerate(sortedlst):
        mapkey[p] = chr(65+i)

    for p in primes:
        out = out+str(mapkey[int(p)])
    
    return out

T = int(input())
for i in range(T):
  _ = input()
  S = [int(n) for n in input().split()]
  text = sol(S)
  print("Case #{}: {}".format(i+1, text))



# print(sol([21,21,21,21,49,49,49,49,49,49, 217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]))
# print(sol([49, 217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]))