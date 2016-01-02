def listMax():
	N, M = [int(n) for n in raw_input().split(" ")]
	List = [0]*N

	for i in range(0,M):
		a,b,k = [int(n) for n in raw_input().split(" ")]
		for j in range(a-1,b):
			List[j] += k
	print max(List)

listMax()



