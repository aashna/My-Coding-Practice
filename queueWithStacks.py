class stackNode(object):

	def _init_(self, data):
		self.data = data
		self.next = None


class stack(object):

	def _init_(self):
		self.top = stackNode(None)
		self.size = size = 0

	def push(data):
		new_node = stackNode(data)
		new_node.next = self.top
		self.top.next = new_node
		self.size += 1

	def pop(self):
		popped = self.top
		self.top = self.top.next
		self.size -= 1
		return popped


class queue(object):

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, data):
		 self.stack1.append(data)
	def dequeue(self):
		if not self.stack2:
			while self.stack1:
			   self.stack2.append(self.stack1.pop())
		return self.stack2.pop()

q = queue()

for i in range(1,5):
 q.enqueue(i)
 print 'Queue ',i,
print ''
for i in range(1,5):
   print 'Dequeue ', q.dequeue(),





 
