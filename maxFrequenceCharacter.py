def maxFrequencyCharacter(string):
	string = list(string)
	hashFunc = {}

	for character in string:
		if character in hashFunc.keys():
		    hashFunc[character]+=1
		else:
			hashFunc[character] = 1
	for key,val in hashFunc.items():
		if val == max(hashFunc.values()):
			return key	

print maxFrequencyCharacter('elephant')