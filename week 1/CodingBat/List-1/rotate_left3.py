def rotate_left3(nums):
  p = nums[0]
  nums[0]=nums[1]
  nums[1]=nums[2]
  nums[2]=p
  return nums