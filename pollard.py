#add pollard rho here (geeks for geeks)

# Python 3 program to find a prime factor of composite using
# Pollard's Rho algorithm

import math

def func(a):
	x = a*a + 1
	return x
# method to return prime divisor for n
def PollardRho(n):

	# no prime divisor for 1
	if (n == 1):
		return n

	# even number means one of the divisors is 2
	if (n % 2 == 0):
		return 2

	# Initialize candidate divisor (or result)
	d = 1
	x = 2
	y = 2

	# until the prime factor isn't obtained.
	# If n is prime, return n
	while (d == 1):

		# Tortoise Move: x(i+1) = f(x(i))
		x = (func(x))%n
		
		# Hare Move: y(i+1) = f(f(y(i)))
		y = (func(y))%n
		y = (func(y))%n

		# check gcd of |x-y| and n
		d = math.gcd(abs(x - y), n)

		# retry if the algorithm fails to find prime factor
		# with chosen x and c
		if (d == n):
			return n

	return d

# Driver function
if __name__ == "__main__":
	n = 85768
	m = n
	f = []
	while m != 1:
		a = PollardRho(m)
		f.append(a)
		m = m // a
		
	print("Factors of", n, "are", f)


# This code is contributed by chitranayal