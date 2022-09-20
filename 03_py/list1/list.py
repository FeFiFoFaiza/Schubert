def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

def make_pi():
  pi = [3, 1, 4]
  return pi

def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

def sum3(nums):
  return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  store = nums[0]
  for i in range(len(nums)-1):
    nums[i] = nums[i+1]
  nums[-1] = store
  return nums

def rotate_left3(nums):
  store = nums[0]
  for i in range(len(nums)-1):
    nums[i] = nums[i+1]
  nums[-1] = store
  return nums
