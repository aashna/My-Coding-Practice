## If buying selling allowed only once  ::: Time complexity: O(n)
def maxDiff(arr):
	min_price = arr[0]
	max_diff = arr[1]-arr[0]

	for i in range(len(arr)):
		if arr[i]-min_price > max_diff:
			max_diff = arr[i] - min_price
		if arr[i] < min_price:
			arr[i] = min_price
	return max_diff

def maxProfit(arr):
	buy = -1

	for i in range(len(arr)-1):
		if buy == -1 and arr[i+1]>arr[i]:
			buy = i
			print 'Buy on day ',i
		if buy!=-1 and arr[i+1]<arr[i]:
			profit = arr[i] - arr[buy]
			buy = -1
			print 'Sell on day ',i
	if buy != -1:
		profit = arr[len(arr)-1] - arr[buy]
		print 'Sell on day ',(len(arr)-1)


#print maxDiff([2,3,10,6,4,8,1])
maxProfit([00, 180, 260, 310, 40, 535, 695])