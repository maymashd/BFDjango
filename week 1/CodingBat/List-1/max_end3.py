def max_end3(nums):
  m=0
  if nums[0]>nums[2]:
    m = nums[0]
  else:
    m = nums[2]
  nums[0]=m
  nums[1]=m
  nums[2]=m
  return nums