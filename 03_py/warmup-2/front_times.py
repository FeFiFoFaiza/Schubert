def front_times(str, n):
  str_len = 3
  if str_len > len(str):
    str_len = len(str)
  front = str[:str_len]
  
  ans = ""
  for i in range(n):
    ans += front
  return ans