def merge(n1,n2):
	""" 
	Merges two numbers
	>>> merge(31, 42)
	4321
	>>> merge(21, 0)
	21
	>>> merge (21, 31)
	3211
	"""

	if n1 == 0 or n2 == 0:
		return n2 if n1==0 else n1

	else:
		if n1 % 10 <= n2 % 10:
			smallest_digit = n1 % 10
			n1 = n1 // 10
		else:
			smallest_digit = n2 % 10
			n2 = n2 // 10
		return smallest_digit + merge(n1,n2)*10

	#merge(42,31)-> 
	#1 + merge(42,3)*10->
	#1+ (2+merge(4,3)*10)*10 ->
	#1+ (2+(3+merge(4,0)*10)*10)*10 ->

			

def count_partition(n,m):

	if n<0 or m==0:
		return 0
	elif n == 0:
		return 1

	return count_partition(n-m,m)+count_partition(n,m-1)

def hailstone(n):
	"""
	Print out the hailstone sequence starting at n, and 			
	return the number of elements in the sequence.
		>>> a = hailstone(10)
		10
		5
		16
		8
		4
		2
		1
		>>> a
		7
	"""
	print(n)
	
	if n == 1:
		return 1
	else:
		n = n//2 if n%2 == 0 else n*3+1
		return 1 + hailstone(n)