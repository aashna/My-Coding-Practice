def powerSet(string):
	curr_list=[""]

	for i in range(0,len(string)):
		for j in range(0,len(curr_list)):
			curr_list.append(curr_list[j]+string[i])
	print curr_list
powerSet("abcd")