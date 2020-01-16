def po(a,b):
    cnt=1
    if b==0:
        return 1
    else:
        for i in range (1,b+1):
            cnt=cnt*a
    return cnt


a=input()
arr=a.split(" ")
print(po(float(arr[0]),int(arr[1])))