import math 
  
def getBegin(P):
    begin = ""
    for r in P:
        if r[0]=="*":
            continue
        b = r.split("*")[0]
        
        lgrB = b if len(b) > len(begin) else begin
        shtB = b if lgrB==begin else begin
        if lgrB.startswith(shtB):
            begin = lgrB
        else:
            return "*"
    return begin

def getEnd(P):
    end = ""
    for r in P:
        if r[-1]=="*":
            continue
        b = r.split("*")[-1]
        
        lgrE = b if len(b) > len(end) else end
        shtE = b if lgrE==end else end
        if lgrE.endswith(shtE):
            end = lgrE
        else:
            return "*"
    return end

import re


def verify(P, S):
    for r in P:
        r = r.replace("*", "[A-Z]*")
        r = "^"+r+"$"
        x = re.search(r, S)
        if x is None:
            return False
        
    return True

def sol(P):
    out = "*"

    
    end = getEnd(P)
    begin = getBegin(P)
    if end=="*" or begin=="*":
        return "*"
    else:
        if verify(P, begin+end):
            return begin+end
        else:
            out = begin
            for r in P:
                sp = r.split("*")
                if r[0]!="*":
                    sp[0]=""
                
                if r[-1]!="*":
                    sp[-1]=""
                
                out += "".join(sp)
            out += end
    return out

T = int(input())
for i in range(T):
  N = int(input())
  P = [input() for n in range(N)]
  text = sol(P)
  print("Case #{}: {}".format(i+1, text))


# sol(["*CONUTS", "*COCONUTS", "*OCONUTS", "*CONUTS"])
# print(sol(["H*O", "HELLO*", "*HELLO", "HE*"]))
# print(sol(["A*B*", "*C*D"]))
# print(sol(["*A*B*", "*C*D*"]))