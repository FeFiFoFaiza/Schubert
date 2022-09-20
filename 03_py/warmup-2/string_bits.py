def string_bits(str):
  ans = ""
  for i in range(len(str)):
    if i % 2 == 0:
      ans += str[i:i+1]
  return ans