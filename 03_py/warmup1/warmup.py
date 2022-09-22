'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we
are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we 
sleep in.
'''
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
print("Test cases for sleep_in")
print(sleep_in(True, True)) # Should return True
print(sleep_in(False, False)) # Should return True
print(sleep_in(True, False)) # Should return False

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each
is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return
True if we are in trouble.
'''
def monkey_trouble(a_smile, b_smile):
  return (a_smile == b_smile)
print("Test cases for mokey_trouble")
print(monkey_trouble(True, True)) # Should return True
print(monkey_trouble(False, False)) # Should return True
print(monkey_trouble(True, False)) # Should return False

'''
Given two int values, return their sum. Unless the two values are the same, then return
double their sum
'''
def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  return a + b
print("Test cases for sum_double")
print(sum_double(1, 2) == 3) # Should be True
print(sum_double(-1, 0) == -1) # Should be True
print(sum_double(3, 3) == 12) # Should be True

'''
Given an int n, return the absolute difference between n and 21, except return double the
absolute difference if n is over 21
'''
def diff21(n):
  if n <= 21:
    return  (21 - n)
  else:
    return 2 * (n - 21)
print(diff21(19) == 2) # Should be True
print(diff21(10) == 11) # Should be True
print(diff21(21) == 0) # Should be True

'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range
0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return
True if we are in trouble
'''
def parrot_trouble(talking, hour):
  return (talking and (hour< 7 or hour > 20))
print("Test cases for parrot_trouble")
print(parrot_trouble(True, 6)) # Should return True
print(parrot_trouble(True, 7)) # Should return False
print(parrot_trouble(False, 6)) # Should return False

'''
Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
'''
def makes10(a, b):
  return (a == 10 or b == 10 or (a + b == 10))
print("Test cases for makes10")
print(makes10(9, 10)) # Should return True
print(makes10(9, 9)) # Should return False
print(makes10(1, 9)) # Should return True

'''
Given an int n, reutrn True if it is within 10 of 100 or 200. NoteL abs(num) computes the
absolute value of a number.
'''
def near_hundred(n):
  return (abs (100 - n) <= 10 or abs (200 - n) <= 10)
print("Test cases for near_hundred")
print(near_hundred(93)) # Should be True
print(near_hundred(90)) # Should be True
print(near_hundred(89)) # Should be False

'''
Given 2 int values, return True if one is negative and one is positive. Except if the
parameter "negative" is True, then return True only if both are negative.
'''
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a< 0 and b >0) or (a > 0 and b < 0))
print("Test cases for pos_neg")
print(pos_neg(1, -1, False)) # Should return True
print(pos_neg(-1, 1, False)) # Should return True
print(pos_neg(-4, -5, True)) # Should return True

'''
Given a string, return a new string where "not" has been added to the front. However, if
the string already begins with "not", return the string unchanged.
'''
def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str
print("Test cases for not_string")
print(not_string('candy') == 'not candy') # Should return True
print(not_string('x') == 'not x') # Should return True
print(not_string('not bad') == 'not bad') # Should return True

'''
Given a non-empty string and an int n, return a new string where the char at index n has
been removed. The value of n will be a valid index of a char in the original string(i.e. n will
be in the range 0..len(str)-1 inclusive)
'''
def missing_char(str, n):
  return str[0:n] + str[n+1:]
print("Test cases for missing_char")
print(missing_char('kitten', 1) == 'ktten') # Should return True
print(missing_char('kitten', 0) == 'itten') # Should return True
print(missing_char('kitten', 4) == 'kittn') # Should return True

'''
Given a string, return a new string where the frist and last chars have been exchanged.
'''
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]
print("Test cases for front_back")
print(front_back('code') == 'eodc') # Should return True
print(front_back('a') == 'a') # Should return True
print(front_back('ab') == 'ba') # Should return True

'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length
is less than 3, the front is whatever is there. Return a new string which is 3 copies of the
front.
'''
def front3(str):
  if len(str) ==0:
    return str
  else:
    return str[0:3] * 3
print("Test cases for front3")
print(front3('Java') == 'JavJavJav') # Should return True
print(front3('Chocolate') == 'ChoChoCho') # Should return True
print(front3('abc') == 'abcabcabc') # Should return True
