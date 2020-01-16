import math
a=int(input())
cnt=0
for i in range(1,int(math.sqrt(a))+1):
    if a%i==0:
        cnt=cnt+1
cnt=cnt*2
if (int(math.sqrt(a))*int(math.sqrt(a)))==a:
    cnt=cnt-1
print(cnt)




