#Counting number of connected components in a undirected graph
#Number of islands
#Friend circles
#Complexity = O(row*column)
def countFriends(friends):
	N = len(friends)
	visited = [[0]*N]*N
	count = 0

	for i in range(0,N):
		for j in range(0,N):
			if friends[i][j] and not visited[i][j]:  #check if i and j are friends and have not been visited
				findNeighbourFriends(friends,i,j,visited)
				count+=1
	return count

def findNeighbourFriends(friends,row_idx, col_idx,visited):

	neighbourRow = [-1, -1, -1,  0, 0,  1, 1, 1]     # neighbouring 8 row indices
	neighbourColumn = [-1,  0,  1, -1, 1, -1, 0, 1]  # neighbouring 8 column indices
	visited[row_idx][col_idx] = 1                    # set visited of i and j to 1

	for i in range(0,8):
		new_rowIdx = neighbourRow[i]+row_idx
		new_colIdx =  neighbourColumn[i]+col_idx

		if  new_rowIdx>=0 and new_rowIdx<len(friends) and new_colIdx>=0 and new_colIdx<len(friends):
		  if friends[new_rowIdx][new_colIdx] and not visited[new_rowIdx][new_colIdx]:
			findNeighbourFriends(friends,new_rowIdx, new_colIdx,visited)

friends= [[0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0],
		  [1, 0, 1, 0, 0]
		 ]
print countFriends(friends)

