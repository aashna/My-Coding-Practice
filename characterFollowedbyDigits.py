'''
Given a string with equal number of even characters followed by equal number of digits, write a method to return a string with a character followed by a digit in order of their occurrence.
for eg: Input : abcd1234
Output: a1b2c3d4
'''
def function(string):
  if (len(string)%2)!=0:
  	return None
  def function_util(string1,string2):
  	if len(string1) == 1:
  		return string1+string2
  	return function_util(string1[:len(string1)/2],string2[:len(string2)/2]) + function_util(string1[len(string1)/2:],string2[len(string2)/2:])
  return function_util(string[:len(string)/2],string[len(string)/2:])

print function('abcd1234')