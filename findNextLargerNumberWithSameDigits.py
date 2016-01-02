def findNextNumber(num):
    num = list(num)
    for i in range(len(num)-1,-1,-1):
        if num[i-1] < num[i]:
            break
    if i==0:
        return
    num[i-1:len(num)] = sorted(num[i-1:len(num)])
    temp = num[i-1]
    num[i-1] = num[i]
    num[i] = temp
    return ''.join(num)
print findNextNumber('1234')