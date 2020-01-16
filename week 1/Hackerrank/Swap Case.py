def swap_case(s):
    a = ""
    for l in s:
        if l.islower() == True:
            a+=l.upper()
        else:
            a+=l.lower()
    return a

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print (result)


