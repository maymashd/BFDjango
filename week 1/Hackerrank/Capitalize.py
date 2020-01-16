
def solve(s):
    a=""
    cnt = 0
    for i in s:
        if i==' ':
            cnt = 0
        else:
            cnt += 1
        if cnt==1:
            a+=i.upper()
        else:
            a+=i
    return a

