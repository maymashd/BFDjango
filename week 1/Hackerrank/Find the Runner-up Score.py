import math
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
m = arr[0]
j = 0
for i in range(n):
    if m < arr[i]:
        m = arr[i]
        j = i
cnt = -101
for k in range(n):
    if arr[k]!=m:
        if cnt<arr[k]:
            cnt = arr[k]
print(cnt)
