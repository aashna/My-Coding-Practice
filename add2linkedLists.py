class Node(object):
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=None

def printlinkedlist(head):
    while head:
        print head.data, ' -> ', 
        head = head.next

def size(head):
    count=1
    while head.next:
        count+=1
        head=head.next
    return count

def add(head1,head2,carry):   
    if not head1:
        return None,None
    result = Node()
    result.next,carry = add(head1.next,head2.next,carry)

    if not carry:
        carry=0
    sumList = head1.data + head2.data + carry
    carry = sumList/10
    sumList=sumList%10

    result.data=sumList
    return result,carry


def addCarry(head1,current,carry,result):
    if head1!=current:
        result,carry = addCarry(head1.next,current,carry,result)

        sumList=head1.data+carry
        carry=sumList/10
        sumList%=10

        sumNode = Node(sumList)
        sumNode.next = result
        result = sumNode
    return result,carry


def addLists(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    carry = 0

    if size(head1)==size(head2):
        result,carry = add(head1,head2,carry)
    else:
        diff = abs(size(head1)-size(head2))

        temp = head1

        while temp.next and diff:
            diff-=1
            temp=temp.next        
        result,carry=add(temp,head2,carry)   
        result,carry = addCarry(head1,temp,carry,result)        
    
        if carry:
            carryNode = Node(carry)
            carryNode.next = result
            result = carryNode 
    
    return result

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node (4)
head1.next.next.next.next = Node(5)

head2 = Node(3)
head2.next = Node(2)
head2.next.next = Node(5)
#head2.next.next.next = Node (4)
#head2.next.next.next.next = Node(1)

print 'Adding'
printlinkedlist(head1)
print ''
print ' + '
printlinkedlist(head2)
print ''
print '='
printlinkedlist(addLists(head1,head2))





