def subtractLists(arr1,arr2):
    '''
    for elem in arr2:              Time complexity O(len(arr1)*len(arr2))
        if elem in arr1:
            arr1.remove(elem)
    return arr1
    '''

    #return list(set(arr1)-set(arr2)) #Time complexity O(len(arr1))

    ptr1=0
    ptr2=0

    while arr1[ptr1] and arr2[ptr2]:
        if arr1[ptr1]<arr2[ptr2]:
            ptr1+=1
        elif arr1[ptr1] == arr2[ptr2]:
            del arr1[ptr1]
            ptr1+=1
        else:
            ptr2+=1
        try: 
           arr1[ptr1] and arr2[ptr2]
        except IndexError: 
          return arr1
    

print subtractLists([1,3,4,5,7],[2,3,5])

