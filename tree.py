class Node(object):
        def __init__(self, val):
                self.val=val
                self.left = None
                self.right = None


def checkBST(root,prev):
  if not root is None:
    if checkBST(root.left, prev) is False:
     	return False

    if not prev is None:
        if root.val<=prev.val:
  	       return False

    prev=root

    return checkBST(root.right, prev)
  return True

def createBST(arr):
  n=len(arr)

  if n==0:
    return

  mid=(n-1)/2

  root=Node(arr[mid])
  root.left=createBST(arr[0:mid])
  root.right=createBST(arr[mid+1:n])
  return root    

def printBST(root):

  if root is None:
    return

  printBST(root.left)
  print root.val,
  printBST(root.right)

def isPresent(root,node):
  if root is None:
    return False
  if root.val == node.val:
    return True
  return isPresent(root.left,node) or isPresent(root.right,node)

def commonAncestor(root, n1,n2):
  if root is None:
    return None
  if not isPresent(root,n1) or not isPresent(root,n2):
    return None
  if root.val == n1.val or root.val == n2.val:
    return root
  if isPresent(root.left,n1) != isPresent(root.left,n2):
    return root
  if isPresent(root.left,n1):
    return commonAncestor(root.left,n1,n2)
  else:
    return commonAncestor(root.right,n1,n2)

def isIdentical(root1,root2):
  if root1 is None and root2 is None:
    return True
  if root1 is None or root2 is None:
    return False
  if root1.val != root2.val:
    return False
  return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)

def isSubTree(root1,root2):
  if root1 is None:
    return False
  if root2 is None:
    return True
  if root1.val == root2.val:
    return isIdentical(root1,root2)
  return isSubTree(root1.left,root2) or isSubTree(root1.right,root2)

def sumtoPath(root,Sum,path,pathList):
  print 'Sum = ',Sum

  if Sum == 0:
    pathList.append(path)
  print 'pathList = ',pathList

  if root is None:
    return
  print 'root = ',root.val

  if root.val<Sum or root.val == Sum:
    path.append(root.val)
    print path
    sumtoPath(root.left,Sum-root.val,path,pathList)
    sumtoPath(root.right,Sum-root.val,path,pathList)
  else:
    sumtoPath(root.left,Sum,path,pathList)
    sumtoPath(root.right,Sum,path,pathList)

  return pathList

root=Node(8)
root.right=Node(9)
root.left=Node(7)
root.left.left=Node(6)
#prev=Node(None)
#print checkBST(root,prev)
#printBST(root)
#printBST(createBST([3,5,9,10,14,16,17]))
#print commonAncestor(root,Node(7),Node(9))
#root2 = Node(15)
#root2.left=Node(13)
#root2.right=Node(8)
#root2.right.right=Node(9)
#root2.right.left=Node(7)
#root2.right.left.left=Node(6)
#printBST(root2)
#print isSubTree(root2,root)
root3 = Node(1)
root3.right=Node(3)
root3.left=Node(2)
root3.left.left=Node(6)
root3.left.right=Node(7)
root3.right.left=Node(4)
root3.right.right=Node(5)
root3.right.left.left=Node(4)
root3.right.left.right=Node(9)
print sumtoPath(root3,9, [],[])




