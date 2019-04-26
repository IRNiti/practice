class pointer:
	def __init__(self, node):
		self.points_to = node


class node:
	def __init__(self, input):
		self.value = input
		self.next_p = pointer(None)

	def next_node(self):
		return self.next_p.points_to


class linked_list:

	def __init__(self, input):
		self.start = node(input)


	def add_node(self, input):
		new_node = node(input)
		current_node = self.start
		while current_node.next_p.points_to is not None:
			current_node = current_node.next_node()
		current_node.next_p = pointer(new_node)


#TODO: implement case when node to remove is the last node or if only one node and that node not equal to input
	def remove_node(self, input):
		if(self.start.value == input):
			if(self.start.next_p.points_to is not None):
				temp = self.start
				self.start = self.start.next_node()
				temp.next_p = pointer(None)
			else: 
				self.start = None
		else:
			current_node = self.start
			nxt_node = current_node.next_node()
			while nxt_node.next_p.points_to is not None:
				if (nxt_node.value == input):
					current_node.next_p.points_to = nxt_node.next_node()
					nxt_node.next_p = pointer(None)
				else:
					current_node = nxt_node
					nxt_node = nxt_node.next_node()
			


	def display_data(self):
		current_node = self.start
		while current_node.next_p.points_to is not None:
			print(current_node.value)
			current_node = current_node.next_node()
		print(current_node.value)





test = linked_list('1')
test.add_node('2')
test.add_node('3')
test.add_node('4')
test.display_data()
test.remove_node('3')
test.display_data()