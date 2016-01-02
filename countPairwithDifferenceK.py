def countPairs(arr,diff):
    arr.sort()
    hashFunc = [0]*(max(arr)+1)
    count = 0

    for elem in arr:
        hashFunc[elem] += 1
    for index,val in enumerate(hashFunc):
        if index > 0:
            hashFunc[index]-=1
            try: 
                  if hashFunc[index+diff] >0:
                    if diff == 0:
                       count+=hashFunc[index]
                       hashFunc[index]=0
                    else: count+=1
            except IndexError: 
              continue
    return count
print countPairs([2,3,4],0)