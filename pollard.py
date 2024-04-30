import math

def func(a):
	x = a*a + 1
	return x

def PollardRho(n):
	if (n == 1):
		return n

	if (n % 2 == 0):
		return 2

	d = 1
	x = 2
	y = 2

	while (d == 1):
		x = (func(x))%n
		y = (func(y))%n
		y = (func(y))%n
		d = math.gcd(abs(x - y), n)
		if (d == n):
			return n
	return d

def find_prime_factors(n):
	m = n
	f = []
	while m != 1:
		a = PollardRho(m)
		f.append(a)
		m = m // a
	if len(f) == 1:
		return 'prime'
	return f

def run_on_range(start, end):
    results = {}
    for number in range(start, end + 1):
        prime_factors = find_prime_factors(number)
        results[number] = prime_factors
    return results

results = run_on_range(1, 500)

for number, prime_factors in results.items():
    print(f"Number {number}: Prime factors: {prime_factors}")

