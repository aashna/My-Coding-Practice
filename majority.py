def majority(arr):
    hashFunc = [0]*(max(arr)+1)

    if not arr:
        return None

    for elem in arr:
        hashFunc[elem]+=1
        if hashFunc[elem]>len(arr)/2:
            return elem
    return None

print majority([3,4])
