def count_evens(nums):
  ctr = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      ctr += 1
  return ctr