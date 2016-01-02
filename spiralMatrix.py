def printSpiral(arr,m,n):

	startRow = 0
	startColumn = 0
	endRow = m
	endColumn = n

 	while startRow-1<endRow and startColumn-1<endColumn:

 		# print 1st row
 		for j in range(startRow,endColumn+1):
 			print arr[startRow][j] ,
 		print " ",

 		startRow += 1

 		#print last column
 		for i in range(startRow,endRow+1):
 			print arr[i][endColumn] ,
 		print " ",

 		endColumn -= 1

 		if startRow < endRow:

 		  #print last row
 		  for j in range(endColumn,startColumn-1,-1):
 		    	print arr[endRow][j] ,
 		  endRow -= 1
 		print " ",

 		if startColumn < endColumn:
 		    #print first column
 		    for i in range(endRow,startRow-1,-1):
 			    print arr[i][startColumn],
 		    startColumn +=1
 		print " ",

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]
printSpiral(arr,2,3)

