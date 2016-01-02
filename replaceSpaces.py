def replace_spaces(string):
	print string
	string=list(string)
	length=len(string)
	i=length
	spaces=0

	while i!=0:
		if string[i-1] is ' ':
		   spaces+=1
		   string.append(' ')
		   string.append(' ')
		i-=1
		   

	l=len(string)

	while length!=0:
		if string[length-1]!= ' ':
			string[l-1]=string[length-1]
			l-=1
		else:
			string[l-1]='0'
			string[l-2]='2'
			string[l-3]='%'
			l-=3
		length-=1
	return "".join(string)

print replace_spaces('my name is')
		
  