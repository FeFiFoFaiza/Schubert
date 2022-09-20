def big_diff(nums):
  minVal = nums[0]
  maxVal = nums[0]
  for i in range(len(nums)):
    minVal = min(minVal, nums[i])
    maxVal = max(nums[i], maxVal)
  return maxVal - minVal