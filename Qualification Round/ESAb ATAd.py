import sys

with open("out", 'w') as outfile:

    def ask(qidx, n):
        
        print(n)
        sys.stdout.flush()
        s = input()
        outfile.write("QUERY: #{}: {}=>{}\n".format(str(qidx), str(n), s))
        
        if s=="N":
            sys.exit(1)

        qidx += 1
        # if qidx > 150:
        #     sys.exit(0)

        return qidx, s

    def complements(bins):
        o = []
        for b in bins:
            if b=="1":
                o.append("0")
            elif b=="0":
                o.append("1")
            else:
                o.append("-")

        return o

    def reverse(bins):
        return bins[::-1]

    def solve(B):
        # bins = ["0"*B]
        # qidx = 0
        # for b in range(1, B*2+1):
        #     qidx, s = ask(qidx, 1)
        # return "".join(bins)
        bins = ["-" for i in range(B)]
        qidx = 0

        # Find reference values
        same = None
        diff = None
        for i in range(1, B//2+1):

            qidx1, a = ask(qidx, i)
            qidx2, b = ask(qidx1, B-i+1)
            qidx = qidx2

            if (qidx1-1)//10 != (qidx2-1)//10:
                qidx, a = ask(qidx, i)

            if diff is None and a!=b:
                diff = (i, B-i+1)
                
            if same is None and a==b:
                same = (i, B-i+1)
            
            if (diff is not None) and (same is not None):
                break
        
        if diff is None:
            outfile.write("NO DIFF CASE\n")
            qidx, a = ask(qidx, same[0])

            bins[same[0]-1] = a
            bins[same[1]-1] = a

            outfile.write("READY: {}".format("".join(bins))+"\n")
            
            for i in range(1, B+1):
                if (qidx)%10==0:
                    qidx, a = ask(qidx, same[0])

                    if (bins[same[0]-1] != a):
                        bins = complements(bins)
                
                done = True
                for j, v in enumerate(bins):
                    if bins[j]=="-":
                        qidx, x = ask(qidx, j+1)
                        bins[j] = x
                        bins[B-j-1] = x
                        done = False

                        outfile.write("ASK q{} idx{} val{}".format(qidx, j, x)+"\n")
                        outfile.write("CHANGE: {}".format("".join(bins))+"\n")
                        break
                if qidx > 149:
                    break
                if done:
                    break
        elif same is None:
            outfile.write("NO SAME CASE\n")
            qidx, b = ask(qidx, diff[0])

            bins[diff[0]-1] = b
            bins[diff[1]-1] = "1" if b=="0" else "0"

            outfile.write("READY: {}".format("".join(bins))+"\n")
            
            for i in range(1, B+1):
                if (qidx)%10==0:
                    qidx, b = ask(qidx, diff[0])

                    if (bins[diff[0]-1] != b):
                        bins = reverse(bins)
                
                done = True
                for j, v in enumerate(bins):
                    if bins[j]=="-":
                        qidx, x = ask(qidx, j+1)
                        bins[j] = x
                        bins[B-j-1] = "1" if x=="0" else "0"
                        done = False

                        outfile.write("ASK q{} idx{} val{}".format(qidx, j, x)+"\n")
                        outfile.write("CHANGE: {}".format("".join(bins))+"\n")
                        break
                if qidx > 149:
                    break
                if done:
                    break
        else:
            
            # GET reference values
            qidx1, a = ask(qidx, same[0])
            qidx2, b = ask(qidx1, diff[0])
            qidx = qidx2

            if (qidx1-1)//10 != (qidx2-1)//10:
                qidx, a = ask(qidx, same[0])

            bins[same[0]-1] = a
            bins[same[1]-1] = a
            bins[diff[0]-1] = b
            bins[diff[1]-1] = "1" if b=="0" else "0"

            outfile.write("MARK A{} B{}".format(same[0]-1, diff[0]-1)+"\n")

            outfile.write("READY: {}".format("".join(bins))+"\n")
            
            while True:
                if (qidx)%10==0:
                    qidx1, a = ask(qidx, same[0])
                    qidx2, b = ask(qidx1, diff[0])
                    qidx = qidx2

                    # if qidx1//10 != qidx2//10:
                    #     qidx, a = ask(qidx, same[0])

                    outfile.write("DISK A{} B{}".format(bins[same[0]-1], bins[diff[0]-1])+"\n")
                    outfile.write("GET A{} B{}".format(a, b)+"\n")

                    if (bins[same[0]-1] == a) and (bins[diff[0]-1] == b):
                        continue
                    elif (bins[same[0]-1] == a) and (bins[diff[0]-1] != b):
                        outfile.write("BF REVERSE: {}".format("".join(bins))+"\n")
                        bins = reverse(bins)
                        outfile.write("AF REVERSE: {}".format("".join(bins))+"\n")
                    elif (bins[same[0]-1] != a) and (bins[diff[0]-1] != b):
                        outfile.write("BF COMPLEMENT: {}".format("".join(bins))+"\n")
                        bins = complements(bins)
                        outfile.write("AF COMPLEMENT: {}".format("".join(bins))+"\n")
                    else:
                        outfile.write("BF REVERSE&COMP: {}".format("".join(bins))+"\n")
                        bins = reverse(bins)
                        bins = complements(bins)
                        outfile.write("AF REVERSE&COMP: {}".format("".join(bins))+"\n")
                
                done = True
                for j, v in enumerate(bins):
                    if bins[j]=="-":
                        qidx, x = ask(qidx, j+1)
                        bins[j] = x
                        done = False

                        outfile.write("ASK q{} idx{} val{}".format(qidx, j, x)+"\n")
                        outfile.write("CHANGE: {}".format("".join(bins))+"\n")
                        break

                if qidx > 149:
                    break
                if done:
                    break

        
        return "".join(bins)

    T, B = [int(n) for n in input().split()]
    for _ in range(T):
        outfile.write("--------START-----------\n"+"\n")
        s = solve(B)
        outfile.write("OUT: {}".format(s)+"\n")
        print(s.replace("-", s[0]))
        # print(s)

        sys.stdout.flush()
        s = input()

        if s =="N":
            sys.exit(1)

        

    sys.exit(0)