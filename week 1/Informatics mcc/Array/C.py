import array

n=int(input())
a=input()
arr=a.split(" ")
cnt=0
for i in range(0,len(arr)):
    if (int(arr[i])>0):
        cnt=cnt+1

print(cnt)