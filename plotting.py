import time
import matplotlib.pyplot as plt
import brute_force
import fermat
import pollard
import Dixon

# Range of numbers to test
start = 1
end = 10_000

# Function to measure time for a given factorization method
def measure_time(factorization_function, n):
    start_time = time.time()
    factorization_function(n)
    return time.time() - start_time

# Collecting data for plotting
times_brute_force = []
times_fermat = []
times_pollard = []
times_dixon = []
prime_factors_count = {}

for n in range(start, end + 1):
    # Measure time for each factorization algorithm
    times_brute_force.append(measure_time(brute_force.prime_factors, n))
    times_fermat.append(measure_time(fermat.find_prime_factors, n))
    times_pollard.append(measure_time(pollard.find_prime_factors, n))
    times_dixon.append(measure_time(Dixon.dixon_factorization, n))

    # Record the count of prime factors
    prime_factors_count[n] = {
        'brute_force': len(brute_force.prime_factors(n)),
        'fermat': len(fermat.find_prime_factors(n)),
        'pollard': len(pollard.find_prime_factors(n)),
        'dixon': len(Dixon.dixon_factorization(n)),
    }

# Plotting the time complexity for each algorithm
# Brute Force
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), times_brute_force, linestyle='-', marker='o', markersize=3, label='Brute Force')
plt.xlabel('Number')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity for Brute Force Algorithm')
plt.grid(True)
plt.show()

# Fermat
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), times_fermat, linestyle='--', marker='x', markersize=3, label='Fermat')
plt.xlabel('Number')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity for Fermat Algorithm')
plt.grid(True)
plt.show()

# Pollard Rho
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), times_pollard, linestyle='-.', marker='s', markersize=3, label='Pollard Rho')
plt.xlabel('Number')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity for Pollard Rho Algorithm')
plt.grid(True)
plt.show()

# Dixon
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), times_dixon, linestyle=':', marker='^', markersize=3, label='Dixon')
plt.xlabel('Number')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity for Dixon Algorithm')
plt.grid(True)
plt.show()

# Plotting the prime factor count for each algorithm
# Brute Force
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), [prime_factors_count[n]['brute_force'] for n in range(start, end + 1)], linestyle='-', marker='o', markersize=3, label='Brute Force')
plt.xlabel('Number')
plt.ylabel('Number of Prime Factors')
plt.title('Prime Factor Count for Brute Force Algorithm')
plt.grid(True)
plt.show()

# Fermat
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), [prime_factors_count[n]['fermat'] for n in range(start, end + 1)], linestyle='--', marker='x', markersize=3, label='Fermat')
plt.xlabel('Number')
plt.ylabel('Number of Prime Factors')
plt.title('Prime Factor Count for Fermat Algorithm')
plt.grid(True)
plt.show()

# Pollard Rho
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), [prime_factors_count[n]['pollard'] for n in range(start, end + 1)], linestyle='-.', marker='s', markersize=3, label='Pollard Rho')
plt.xlabel('Number')
plt.ylabel('Number of Prime Factors')
plt.title('Prime Factor Count for Pollard Rho Algorithm')
plt.grid(True)
plt.show()

# Dixon
plt.figure(figsize=(12, 8))
plt.plot(range(start, end + 1), [prime_factors_count[n]['dixon'] for n in range(start, end + 1)], linestyle=':', marker='^', markersize=3, label='Dixon')
plt.xlabel('Number')
plt.ylabel('Number of Prime Factors')
plt.title('Prime Factor Count for Dixon Algorithm')
plt.grid(True)
plt.show()
