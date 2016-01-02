class Node(object):
        def __init__(self, data=None, next_node=None):
                self.data=data
                self.next_node = next_node

        def get_data(self):
                return self.data

        def get_next(self):
                return self.next_node

        def set_next(self, new_next):
                self.next_node = new_next

class LinkedList(object):
        def __init__(self, head=None):
               self.head = head

        def insert(self, data):
               new_node = Node(data)
               Node(self.head).set_next(new_node)
               print 'inserted ',data

        def size(self):
               current = self.head
               count = 0
               while current:
                 count += 1
                 current = current.get_next()
               return count

        def search(self, data):
               current = self.head
               found = False
               while current and found is False:
                  if current.get_data() == data:
                    found = True
                  else:
                     current = current.get_next()
               if current is None:
                   raise ValueError("Data not in list")
               return current
    
        def printLL(self):
               current=self.head

               while not current is None:
                  print Node(current).get_data(),
                  current = Node(current).next_node

        def delete(self, data):
               current = self.head
               previous = None
               found = False
            
               while current and found is False:
                 if current.get_data() == data:
                   found = True
                 else:
                   previous = current
                   current = current.get_next()
                 if current is None:
                   raise ValueError("Data not in list")
                 if previous is None:
                   self.head = current.get_next()
                 else:
                   previous.set_next(current.get_next())


def remove_duplicates(node):
  existing_values = set([node.data])

  while not node.next_node is None:
    next = node.next_node
    if next.data in existing_values:
      node.next = next.next_node
    else:
      node = node.next_node
      existing_values.add(node.data)

ll=LinkedList(1)
ll.insert(2)
ll.insert(3)
ll.insert(2)
ll.insert(4)
ll.insert(1)
ll.printLL()