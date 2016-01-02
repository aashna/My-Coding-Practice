def isSubset(arr,sumVal,n):
	if sumVal == 0:
		return True
	if sumVal!=0 and n == 0:
		return False
	if arr[n-1]>sumVal:
		return isSubset(arr,sumVal,n-1)
	return isSubset(arr,sumVal,n-1) | isSubset(arr,sumVal - arr[n-1], n-1)

def allSubsets(arr, currList, idx,nodes, targetSum,currentSum):
	if currentSum == targetSum:
		print 'subset found = ',currList[0:idx]
		print 'nodes = ',nodes
		allSubsets(arr,currList, idx-1,nodes+1,targetSum, currentSum-arr[nodes-1])
	else:
		for i in range(nodes,len(arr)):
			currList.append(arr[i])
			print 'currList = ',currList
			allSubsets(arr,currList, idx+1,i+1,targetSum,currentSum+arr[i])





#print isSubset([2,3,4,5,10],1,5)
print allSubsets([2,3,4,5,10],[],0,0,9,0)
