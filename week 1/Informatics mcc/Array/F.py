import array

n=int(input())
a=input()
arr=a.split(" ")
cnt=0
for i in range(1,len(arr)-1):
    if (int(arr[i])>int(arr[i-1]) and int(arr[i])>int(arr[i+1])  ):
        cnt+=1

if n<3:
    print("0")
else:
    print(cnt)