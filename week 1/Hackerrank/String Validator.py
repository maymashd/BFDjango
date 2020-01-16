if __name__ == '__main__':
    s = raw_input()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for i in range(len(s)):
        if s[i].isalnum():
            c1+=1
        if s[i].isalpha():
            c2+=1
        if s[i].isdigit():
            c3+=1
        if s[i].islower():
            c4+=1
        if s[i].isupper():
            c5+=1
if c1>0:
    print(True)
else:
    print(False)
if c2>0:
    print(True)
else:
    print(False)
if c3>0:
    print(True)
else:
    print(False)
if c4>0:
    print(True)
else:
    print(False)
if c5>0:
    print(True)
else:
    print(False)
