def find(arr,number):
	i = 0
	n=len(arr)

	while(True):
		if i>n:
			return -1
		elif arr[i]==number:
			return i 
		else:
			i+=1

print find([7,2,5,10,1,0,8,4],4)


