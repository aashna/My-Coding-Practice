def intersection(arr1,arr2):
    ptr1=0
    ptr2=0

    if not arr1 or not arr2:
        return None

    try:
        arr1[ptr1] and arr2[ptr2]
        while ptr2<len(arr2):
            if arr1[ptr1]<arr2[ptr2]:
                del arr1[ptr1]
            elif arr1[ptr1]>arr2[ptr2]:
                ptr2+=1
            elif arr1[ptr1]==arr2[ptr2]: 
                ptr1+=1
                ptr2+=1
    except IndexError: 
        return arr1

def union(arr1,arr2):
    ptr1=0
    ptr2=0

    if not arr2:
        return arr1
    if not arr1:
        return arr2
    try:
        arr1[ptr1] and arr2[ptr2]
        while ptr2<len(arr2):
           if arr1[ptr1]<arr2[ptr2]:
                ptr1+=1
           elif arr1[ptr1]>arr2[ptr2]:
                ptr2+=1
           elif arr1[ptr1]==arr2[ptr2]: 
                del arr1[ptr1]
                ptr2+=1
        print arr1,arr2
    except IndexError: 
        return arr1+arr2

print 'Intersection =',intersection([1,2,3,4,5,9],[2,8,9,10])
print 'Union =',union([1,2,3,4,5,9],[10])