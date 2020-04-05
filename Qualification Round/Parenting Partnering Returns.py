 
def overlap(taska, taskb):
    # print(taska, taskb)
    start_a, end_a, i = taska
    start_b, end_b, j = taskb

    if (start_b == start_a) and (end_a == end_b):
        return True

    if start_a < start_b < end_a:
        return True

    if start_a < end_b < end_a:
        return True

    if start_b < start_a < end_b:
        return True

    if start_b < end_a < end_b:
        return True
    
    

    # print(taska, taskb, "NOT_OVERLAPPED")
    return False

def sol(tasks):
    o = ["" for i in range(len(tasks))]
    
    C = tasks[0]
    J = None

    o[tasks[0][2]]="C"
    for idx in range(1, len(tasks)):
        task = tasks[idx]
        if overlap(C, task):
            if J is None:
                J = task
                o[task[2]] = "J"
            elif overlap(J, task):
                return "IMPOSSIBLE"
            else:
                J = task
                o[task[2]] = "J"
        else:
            C = task
            o[task[2]] = "C"
            
    return "".join(o)
    
def newcmp(a):
    return a[0]


assert (overlap((0, 100, 0), (100, 200, 1)) == False)
assert (overlap((0, 100, 0), (50, 200, 1)) == True)
assert (overlap((0, 100, 0), (50, 60, 1)) == True)
assert (overlap((0, 100, 0), (0, 50, 1)) == True)
assert (overlap((0, 100, 0), (0, 100, 1)) == True)
assert (overlap((0, 100, 0), (0, 200, 1)) == True)
assert (overlap((50, 100, 0), (0, 20, 1)) == False)
assert (overlap((50, 100, 0), (0, 50, 1)) == False)
assert (overlap((50, 100, 0), (0, 70, 1)) == True)
assert (overlap((50, 100, 0), (0, 100, 1)) == True)
assert (overlap((50, 100, 0), (0, 160, 1)) == True)

T = int(input())
for p in range(T):
  N = int(input())

  tasks = []
  for i in range(N):
      s, t = [int(n) for n in input().split()]
      tasks.append((s, t, i))

  tasks = sorted(tasks, key=newcmp)
  o = sol(tasks)
  print("Case #{}: {}".format(p+1, o))

# print(sol([(360,480, 0), (600,660, 1), (420,540, 2)]))
# print(sol([(1,1440, 0), (1,3, 1), (2,4, 2),]))
