def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) \
        	if l[j][-1] < d[i]] or [[]],\
        	 key=len) 
                  + [d[i]])
    print 'l =',l
    return max(l, key=len)

d= [3,2,6,4,5,1]
print longest_increasing_subsequence(d)