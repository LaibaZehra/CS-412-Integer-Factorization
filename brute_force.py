
def prime_factors(n):
  factors = []
  divisor = 2
  while n > 1:
    while n % divisor == 0:
      factors.append(divisor)
      n //= divisor
    divisor += 1
  return factors

def main():
  n = 20
  factors = prime_factors(n)
  print(f"The prime factors of {n} are: {factors}")

if __name__ == "__main__":
  main()
