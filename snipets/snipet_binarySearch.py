
# binary search

#%%

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
	n = len(input_array)
	i, j = 0, n
	while j >= i: # consider i==j too !
		m = int((j+i)/2)
		if input_array[m] == value:
			return m
		elif input_array[m] < value:
			# must go right
			i = m+1
		else:
			# must go left
			j = m-1
	return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)