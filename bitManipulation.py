def merge(N,M,j,i):

	left = 1<<(j+1)
	right = (1<<i)-1
	mask = left|right

	return (N & mask)|(M << i)

print 'N = ',"{0:b}".format(63),
print 'M = ',"{0:b}".format(10)
print 'Result = ',"{0:b}".format(merge(63,10,4,1))