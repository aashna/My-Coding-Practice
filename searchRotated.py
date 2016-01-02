def search(arr, start, last, elem):

	if last<start:
		return -1

	mid = (start + last)/2

	if elem == arr[mid]:
		return mid

	if elem == arr[start]:
		return start
	if elem == arr[last]:
		return last
		
	if arr[start] < arr[mid]:  #first half sorted
		if elem > arr[start] and elem < arr[mid]:
			return search(arr, start, mid-1, elem)  #if elem present in first half
		else:
			return search(arr, mid+1 ,last, elem)  #if elem in second half
	else: #first half not sorted
		if elem > arr[mid] and elem<arr[last]:
			return search(arr,mid+1,last,elem)
		else:
			return search(arr,start,mid-1,elem)

print search([5,6,7,8,1,2,3,4] , 0, 7, 1)

