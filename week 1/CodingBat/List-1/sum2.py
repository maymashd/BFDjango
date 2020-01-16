def sum2(nums):
  l = len(nums)
  if l==0:
    return 0
  elif l==1:
    return nums[0]
  else:
    return nums[0]+nums[1]