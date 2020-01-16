

def wrap(string, max_width):
    a=[]
    for i in range(0,len(string),max_width):
        a.append(string[i:i+max_width])
    b = "\n".join(a)
    return b


