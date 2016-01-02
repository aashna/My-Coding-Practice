def string_reverse_with_extra_memory(string):
 length=len(string)
 result=""
 i=0

 while length!=0:
    result+=string[length-1]
    length=length-1
 return result



def string_reverse_in_place(string):
	ptr1=0
	ptr2=len(string)-1

	string=list(string)

	while ptr1<ptr2:
		temp=string[ptr1]
		string[ptr1]=string[ptr2]
		string[ptr2]=temp
		ptr1+=1
		ptr2-=1
	return "".join(string)


string="aashna"
print string_reverse_with_extra_memory(string) #O(n) time O(n) space
print string_reverse_in_place(string) #O(n) time constant space
print string[::-1]
s=list(string)
s.reverse()
print "".join(s) #O(n)