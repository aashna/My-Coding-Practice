class Node(object):
    def __init__(self, data=None, next_node=None,rand_node=None):
        self.data=data
        self.next_node = next_node
        self.rand_node = rand_node

def cloneLinkedList(head):
    temp_node = head
    nextNode = temp_node.next_node
    clone_head = Node(head.data)
    prev = clone_head
    temp_node.next = clone_head.next_node

    while temp_node.next_node:
        new_node = Node(temp_node.data)
        nextNode = temp_node.next_node
        temp_node.next_node = new_node
        new_node.rand_node=temp_node
        prev.next_node = new_node
        temp_node = nextNode

    clone_temp = clone_head
    clone_prev = clone_head

    while clone_temp.next_node:
        clone_prev.next_node = clone_temp
        clone_temp.rand_node = clone_temp.rand_node.rand_node.next_node
        clone_temp=clone_temp.next_node
    return clone_head

def printlinkedlist(head):
    while head.next_node:
        print head.data,head.next_node.data,head.rand_node.data
        head = head.next_node

head = Node(1)
head.next_node = Node(2)
head.next_node.next_node = Node(3)
head.next_node.next_node.next_node = Node (4)
head.next_node.next_node.next_node.next_node = Node(5)
head.next_node.next_node.next_node.next_node.next_node=Node()
head.rand_node=head.next_node.next_node
head.next_node.rand_node = head.next_node.next_node.next_node.next_node
head.next_node.next_node.rand_node=head.next_node
head.next_node.next_node.next_node.rand_node=head.next_node.next_node.next_node
head.next_node.next_node.next_node.next_node.rand_node=head.next_node.next_node

print 'Original List = ',printlinkedlist(head)
print 'Cloned List = ',printlinkedlist(cloneLinkedList(head))