import numpy

def numPaths(arr,M,N):
	count  = [[0]*N for i in range(M)]
	print count

	for i in range(0,M):
		count[i][0] = 1
		
	for j in range(0,N):
		count[0][j] = 1

	print count

	for i in range(1,M):
		for j in range(1,N):
			if arr[i][j-1] == 1:
				count[i][j] += count[i][j-1]
			if arr[i-1][j] ==1:
				count[i][j] += count[i-1][j]
			print count

	return count[M-1][N-1]


arr = [[1,1,1],
	   [1,1,1],
	   [1,1,1]]
print numPaths(arr,3,3)

