from math import ceil, sqrt

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

# Fermat's factorization method
def fermat_factors(n):
    # If it's prime or non-positive, return the number itself
    print(n)
    if is_prime(n) or n <= 1:
        return [n]

    # Check if n is an even number
    if n % 2 == 0:
        return [n // 2, 2]

    # Start Fermat's factorization
    a = ceil(sqrt(n))
    while True:
        b1 = a * a - n
        if b1 < 0:
            break
        b = int(sqrt(b1))
        if b * b == b1:
            return [a - b, a + b]
        a += 1
    return [n]

# Function to recursively factorize until prime factors are found
def find_prime_factors(n):
    if is_prime(n) or n == 1:
        return [n]
    factors = fermat_factors(n)
    prime_factors = []

    for factor in factors:
        if is_prime(factor):
            prime_factors.append(factor)
        else:
            prime_factors.extend(find_prime_factors(factor))  # Recursive factorization

    return prime_factors

print(find_prime_factors(270))
# # Function to run the prime factorization for a range of numbers
# def run_on_range(start, end):
#     results = {}
#     for number in range(start, end + 1):
#         prime_factors = find_prime_factors(number)
#         results[number] = prime_factors
#     return results

# # Get prime factors for all numbers from 1 to 1000
# results = run_on_range(1, 500)

# # Display results
# for number, prime_factors in results.items():
#     print(f"Number {number}: Prime factors: {prime_factors}")
