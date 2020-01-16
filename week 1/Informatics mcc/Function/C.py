def po(a,b):
    if ((a==1 and b==0) or (a==0 and b==1)):
        return True
    else:
        return False


a=input()
arr=a.split(" ")
if (po(int(arr[0]),int(arr[1])))==True:
    print(1)
else:
    print(0)