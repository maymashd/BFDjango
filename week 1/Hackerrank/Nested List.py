ln = []
ls = []
for _ in range(int(raw_input())):
    name = raw_input()
    ln.append(name)
    score = float(raw_input())
    ls.append(score)
min1 = min(ls)
min2 = max(ls)
for i in range(len(ls)):
    if ls[i]!=min1:
        if ls[i]<min2:
            min2 = ls[i]
nm =[]
for i in range(len(ls)):
    if ls[i]==min2:
        nm.append(ln[i])
nm.sort()
for i in range(len(nm)):
    print(nm[i])
