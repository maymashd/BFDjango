a=int(input(""))
b=int(input(""))
if (a==0 or b==0):
  print(0)
elif ((a*b)%109==0):
  print(0)
elif (a >= 0):
  print((a*b)%109)
else:
  a=a*(-1)
  print(109-(a*b)%109) 