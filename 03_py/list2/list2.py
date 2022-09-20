def count_evens(nums):
  x = 0
  y = 0
  while x < len(nums):
    if nums[x] % 2 == 0:
      y += 1
    x += 1
  return y

def big_diff(nums):
  x = 1
  bignumber = nums[0]
  smallnumber = nums[0]
  while x < len(nums):
    if nums[x] > bignumber:
      bignumber = nums[x]
    if nums[x] < smallnumber:
      smallnumber = nums[x]
    x += 1
  return bignumber - smallnumber
    
def centered_average(nums):
  x = 1
  bignumber = nums[0]
  smallnumber = nums[0]
  y = nums[0]
  while x < len(nums):
    if nums[x] > bignumber:
      bignumber = nums[x]
    if nums[x] < smallnumber:
      smallnumber = nums[x]
    y += nums[x]
    x += 1
  y = y - bignumber - smallnumber
  y = y / (len(nums)-2)

  return y
  
    

def sum13(nums):
  x = 0
  sum = 0
  while x < len(nums):
    if nums[x] != 13:
      sum += nums[x]
    else:
      x = x + 1
    x += 1
  return sum
    

def sum67(nums):
  x = 0
  sum = 0
  y = 1
  z = 0
  counter = False
  while x < len(nums):
    if nums[x] == 6 and counter == False:
      y = x
      counter = True
    if nums[x] == 7 and counter == True:
      z = x
      counter = False
    while y <= z:
      sum -= nums[y]
      y += 1
    sum += nums[x]
    x += 1
  return sum

def has22(nums):
  x = 1
  pog = False
  while x < len(nums):
    if nums[x-1] == 2 and nums[x] == 2:
      pog = True
    x += 1
  return pog



  
