if __name__ == '__main__':
    N = int(raw_input())
ls = []
s = []
for i in range(N):
    s = raw_input().split()
    if s[0]=='insert':
        ls.insert(int(s[1]),int(s[2]))
    if s[0]=='print':
        print(ls)
    if s[0]=='remove':
        ls.remove(int(s[1]))
    if s[0]=='append':
        ls.append(int(s[1]))
    if s[0]=='sort':
        ls.sort()
    if s[0]=='pop':
        ls.pop()
    if s[0]=='reverse':
        ls.reverse()
