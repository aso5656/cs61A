def count_stair_ways(n):
	"""
	You want to go up a flight of stairs that has n steps. You can either take 1
	or 2 steps each time. How many different ways can you go up this flight of
	stairs?
	"""
	if n == 0 or n ==1:
		return 1
	elif n < 0:
		return 0
	else:
		return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
	"""
	Consider a special version of the count_stairways problem, where instead
	of taking 1 or 2 steps, we are able to take up to and including k steps at
	a time
	>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
	4
	>>> count_k(4, 4)
	8
	>>> count_k(10, 3)
	274
	>>> count_k(300, 1) # Only one step at a time
	1
	"""
	# if n == 0:
	# 	return 1
	# elif n<0 or k == 0 :
	# 	return 0
	# else:
	# 	return count_k(n-k,k) + count_k(n,k-1)
	#in above way, count_k(3,3) returns 3, missing 1+2

	if n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		total = 0
		i = 1
		while i <= k:
			#take 1 to k step first rather than only k-1 first
			total += count_k(n - i, k)
			i += 1
		return total

def even_weighted(s):
	"""
	Write a function that takes a list s and returns a new list that keeps only
	the even-indexed elements of s and multiplies them by their corresponding
	index.
	>>> x = [1, 2, 3, 4, 5, 6]
	>>> even_weighted(x)
	[0, 6, 20]
	"""
	return [s[i]*i for i in range(len(s)) if i%2 ==0]

def max_product(s):
	"""
	Write a function that takes in a list and returns the maximum product that
	can be formed using nonconsecutive elements of the list. The input list will
	contain only numbers greater than or equal to 1.

	Return the maximum product that can be formed using non-consecutive
	elements of s.
	>>> max_product([10,3,1,9,2]) # 10 * 9
	90
	>>> max_product([5,10,5,10,5]) # 5 * 5 * 5
	125
	>>> max_product([])
	1
	"""
	if len(s)==0:
		return 1
	elif len(s)==1:
		return s[0]
	else:
		#If we include the current number, we cannot use the adjacent number.
		#If we don’t use the current number, we try the adjacent number (and obviously ignore the current number)
		return max(s[0] * max_product(s[2:]), max_product(s[1:]))
	
def check_hole_number(n):
	"""
	A hole number is a number in which every other digit dips below the digits immediately adjacent to it.
For example, the number 968 would be considered a hole number because the number 6 is smaller than
both of its surrounding digits. Other hole numbers include 9192959 or 324364989. The number 544 would
not be considered a hole number. For simplicity assume that we only pass in numbers that have an odd
number of digits
	>>> check_hole_number(123)
	False
	>>> check_hole_number(3241968)
	True
	>>> check_hole_number(3245968)
	False
	"""
	if n < 10:
		return True

	else:
		#check first dip and check next dip
		return (n//10%10 < n%10 and n//10%10 < n//100%10) and check_hole_number(n//100)


def check_mountain_number(n):
	"""
	A mountain number is a number in which the digits from right to left increase toward the middle of the
	number (not necessarily the exact middle digit). After the maximum digit has been reached, the digits to
	the left of that maximum digit should strictly decrease. Define the following function so that it properly
	identifies mountain numbers
	>>> check_mountain_number(103)
	False
	>>> check_mountain_number(153)
	True
	>>> check_mountain_number(3241968)
	False
	>>> check_mountain_number(2345986)
	True
	"""
	def func(n,increasing):
		if n < 10:
			return True 
		if increasing and n%10 < n// 10 % 10:
			return func(n//10,increasing)
		
		return (n % 10) > ((n // 10) % 10) and func(n // 10, False)

	return func(n, True)
