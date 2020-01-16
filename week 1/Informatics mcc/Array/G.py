import array

n=int(input())
a=input()
arr=a.split(" ")
cnt=0
for i in range(0,int(len(arr)/2)):
    a=arr[i]
    arr[i]=arr[len(arr)-1-i]
    arr[len(arr) - 1 - i]=a
for i in range(0,len(arr)):
    print(arr[i],end=' ')
