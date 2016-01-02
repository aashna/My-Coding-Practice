####   MERGE SORT  ####

def merge(arr,start,middle,end):
 length1= middle - start +1
 length2= end-middle
 first=[];last=[]
 print 'input array',arr,'start=',start, 'middle=',middle,'end=',end

 first=arr[0:length1]
 last=arr[middle+1:middle+1+length2]
 print 'first=',first
 print 'last=',last

 i=0;j=0;result=[];k=1

 while i<length1 and j<length2:
  print 'first[',i,'] =', first[i]
  print 'last[',j,'] =', last[j]
  if first[i]<=last[j]:
   result.append(first[i])
   i+=1
  else:
   result.append(last[j])
   j+=1

 while i<length1: 
  result.append(first[i])
  i+=1
 while j<length2:
  result.append(last[j])
  j+=1

def mergeSort(arr,start,end):
	if start<end:
		middle=start+(end-1)/2
		print 'start=',start,'end',end,'middle=',middle
		mergeSort(arr,1,middle)
		mergeSort(arr,middle+1,end)
		merge(arr,start,middle,end)
	print arr


arr=[12,11,13,15,6,7]
mergeSort(arr,0,len(arr))