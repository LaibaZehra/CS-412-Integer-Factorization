from math import sqrt, gcd, ceil
import numpy as np

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to recursively find prime factors
def find_prime_factors(n):
    if is_prime(n) or n == 1:
        return [n]
    factors = []
    i = 2
    # Simple factorization
    while i <= sqrt(n):
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Dixon's factorization algorithm
def dixon_factorization(n):
    # Factor base for the given number
    base = [2, 3, 5, 7]
    start = int(sqrt(n))
    pairs = []
    factors = []

    # Find related squares using the factor base
    for i in range(start, n):
        lhs = i**2 % n
        for b in base:
            rhs = b**2 % n
            if lhs == rhs:
                pairs.append([i, b])
                factor = gcd(i - b, n)
                if factor != 1 and factor not in factors:
                    factors.append(factor)

    
    # Calculate GCDs and extract unique factors
    # for p in pairs:
    #     factor = gcd(p[0] - p[1], n)
    #     if factor != 1 and factor not in factors:
    #         factors.append(factor)

    # Recursively find prime factors for all extracted factors
    prime_factors = []
    for factor in factors:
        prime_factors.extend(find_prime_factors(factor))

    return list(np.unique(prime_factors))

# Function to run the prime factorization for a range of numbers
# def run_on_range(start, end):
#     results = {}
#     for number in range(start, end + 1):
#         prime_factors = dixon_factorization(number)
#         results[number] = prime_factors
#     return results

# # Get prime factors for all numbers from 1 to 1000
# results = run_on_range(1, 500)

# # Display results
# for number, prime_factors in results.items():
#     print(f"Number {number}: Prime factors: {prime_factors}")
print(dixon_factorization(20))