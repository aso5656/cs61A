def make_func_repeater(f,x):
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat

def is_prime(n):
    def prime_helper(n,k):
        if n==1 or k ==1:
            return True

        elif n%k ==0:
            return False
        else:
            return prime_helper(n,k-1)

    return prime_helper(n,n-1)

def num_eights(n):
    if n//10 ==0:
        return 0 if n!=8 else 1
    else:
        return num_eights(n//10) if n%10==0 or (n%10%8) != 0 else num_eights(n//10)+1

def missing_digits(n):
    if n//10 == 0:
        return 0
    else:
        c = n%10 - n//10%10
        c = 0 if c<=1 else c-1
        return c + missing_digits(n//10)

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    def helper(left,coin):
        print("DEBUG:",left,coin)
        if left == 0:
            return 1
        elif not coin or left < coin:
            return 0
        else:
            return helper(left-coin,coin)+helper(left,next_largest_coin(coin))
    return helper(total,1)

def path(m,n):
    if m ==1 or n==1:
        return 1
    else:
        return path(m-1,n) + path(m,n-1)

def max_seq(n,t):
    if n*t ==0:
        return 0
    else:
        return max(n%10+max_seq(n//10,t-1)*10, max_seq(n//10,t))

def add_char(w1,w2):
    if len(w1)*len(w2)==0:
        return w2
    elif w1[0] == w2[0]:
        return add_char(w1[1:],w2[1:])
    else:
        return w2[0]+add_char(w1,w2[1:])

def max_product(s):
	if not s:
		return 1
	else:
		return max(s[0]*max_product(s[2:]),max_product(s[1:]))
