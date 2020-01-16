import array

n=int(input())
a=input()
arr=a.split(" ")
cnt=0
ok=False
for i in range(1,len(arr)):
    if (int(arr[i])*int(arr[i-1])>0):
        ok=True

if ok==True:
    print("YES")
else:
    print("NO")