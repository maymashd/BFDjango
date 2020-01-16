def min1(a,b):
    if (a<=b):
        return a
    else:
        return b
def min2(a,b,c,d):
    return min1(min1(a,b),min1(c,d))
a=input()
arr=a.split(" ")
print(min2(int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3])))