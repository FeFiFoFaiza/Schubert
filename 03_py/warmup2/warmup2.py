def string_times(str, n):
  return str * n
  
def front_times(str, n):
  return str[0:3] * n
  
def string_bits(str):
  new = ''
  i = 0
  while i < (len(str)):
    if i % 2 == 0:
      new += str[i]
    i+= 1
  return new
 
def string_splosion(str):
  new = ''
  for i in range(len(str)+1):
    new += str[0:i]
  return new

def last2(str):
  new = str[-2:]
  counter = 0
  for i in range(len(str)-2):
    if (str[i:i+2] == new):
      counter +=1
  
  return counter
  
def array_count9(nums):
  counter = 0
  for i in nums:
    if i == 9:
      counter +=1
  return counter
  
def array_front9(nums):
  if len(nums) < 4:
    for i in nums:
      if i == 9:
        return True
        
    return False
  else:
    for i in range(0,4):
      if nums[i] == 9:
        return True
        
    return False
    
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False
  
