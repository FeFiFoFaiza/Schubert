def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
      
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  
def diff21(n):
  if n <= 21:
    return  (21 - n)
  else:
    return 2 * (n - 21)
   
def parrot_trouble(talking, hour):
  return (talking and (hour< 7 or hour > 20))

def makes10(a, b):
  return (a == 10 or b == 10 or (a + b == 10))
  
def near_hundred(n):
  return (abs (100 - n) <= 10 or abs (200 - n) <= 10)
  
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a< 0 and b >0) or (a > 0 and b < 0))

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str
    
def missing_char(str, n):
  return str[0:n] + str[n+1:]
  
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]
    
def front3(str):
  if len(str) ==0:
    return str
  else:
    return str[0:3] * 3
