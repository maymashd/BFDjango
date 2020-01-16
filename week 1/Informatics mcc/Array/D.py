import array

n=int(input())
a=input()
arr=a.split(" ")
cnt=0
for i in range(1,len(arr)):
    if (int(arr[i])>int(arr[i-1])):
        cnt=cnt+1

print(cnt)