
# fibonacci sequence, recursively

#%%

"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
	if position <= 0:
		return 0
	elif position <= 2:
		return 1
	else:
		return get_fib(position-1) + get_fib(position-2)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(19)
print get_fib(0)
res = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986]
print res[9]
print res[11]
print res[19]
print res[0]