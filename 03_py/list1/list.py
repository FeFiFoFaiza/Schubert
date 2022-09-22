'''
Given an array of ints,
return True if 6 appears as either the first or last element in the array.
The array will be length 1 or more.
'''
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6
print("Test cases for first_last6")
print(first_last6([1,2,6])) # should return True
print(first_last6([1])) # should return True
print(first_last6([3])) # should return False
print(first_last6([2,3,421,513])) # should return False

'''
Given an array of ints,
return True if the array is length 1 or more,
and the first element and the last element are equal.
'''
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False
print("Test cases for same_first_last")
print(same_first_last([1,2,3])) # should return False
print(same_first_last([1,2,3,1])) # should return True
print(same_first_last([7,7])) # should return True
print(same_first_last([])) # should return False

'''
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

'''
def make_pi():
  pi = [3, 1, 4]
  return pi
print("make_pi")
print(make_pi())
print(make_pi() == [3,1,4]) #should return True
'''
Given 2 arrays of ints, a and b,
return True if they have the same first element
or they have the same last element.
Both arrays will be length 1 or more.
'''
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False
print("Test cases for common_end")
a = [1,2,3]
print(common_end(a, [3,2,3])) # should return True
print(common_end(a, [1,2,1])) # should return True
print(common_end(a, [1])) # should return True
print(common_end(a, [2,3,1,41])) # should return False

'''
Given an array of ints length 3, return the sum of all the elements.
'''
def sum3(nums):
  return nums[0] + nums[1] + nums[2]
print("Test cases for sum3")
print(sum3([1,2,3]) == 6) # should return True
print(sum3([34,3,3]) == 40) # should return True

'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
'''

def rotate_left3(nums):
  store = nums[0]
  for i in range(len(nums)-1):
    nums[i] = nums[i+1]
  nums[-1] = store
  return nums
print("Test cases for rotate_left3")
print(rotate_left3([1, 2, 3]) == [2, 3, 1]) # should return True
print(rotate_left3([0, 0, 1]) == [0, 1, 0]) # should return True

