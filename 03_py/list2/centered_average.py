def centered_average(nums):
  minVal = nums[0]
  maxVal = nums[0]
  sum = 0
  for i in range(len(nums)):
    minVal = min(nums[i], minVal)
    maxVal = max(nums[i], maxVal)
    sum += nums[i]
  return (sum - (maxVal + minVal)) / (len(nums) - 2)
