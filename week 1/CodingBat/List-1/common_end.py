def common_end(a, b):
  al = len(a)
  bl = len(b)
  if al>0 and bl>0:
    if a[0]==b[0] or a[al-1]==b[bl-1]:
      return True
    else:
      return False
  else:
    return False