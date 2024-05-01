def is_prime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def prime_factors(n):
  factors = []
  divisor = 2
  while n > 1:
    while n % divisor == 0:
      factors.append(divisor)
      n //= divisor
    divisor += 1
  return factors

# def main():

#   n = 796860999999
#   factors = prime_factors(n)
#   print(f"The prime factors of {n} are: {factors}")

# if __name__ == "__main__":
#   main()
