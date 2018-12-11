
# declare a public vs. private attribute

#%%

class Drink:
    
	def __init__(self, qty, owner):
		# this one is public
		self.qty = qty
        
		# this one will be 'managed':
		# - put it 'hard to access' with name mangling __
		# - redefine its getter and setter
		self.__owner = owner 

    # getter (no its not owner.getter)
	@property
	def owner(self):
		return self.__owner

    # setter
	@owner.setter
	def owner(self, *args):
		raise ValueError('owner attribute cannot be changed')


d = Drink(25, 'Tom')
print(d.__dict__)
		
d.qty = 50 # want more!
print(d.__dict__)

d.owner = 'this unkown guy' # do not share drinks!
print(d.__dict__)




