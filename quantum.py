import math
import random

# Function to compute the greatest common divisor (GCD) using Euclid's Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to find the smallest r such that a^r ≡ 1 (mod n)
def find_order(a, n):
    for r in range(1, n):
        if pow(a, r, n) == 1:
            return r
    return None

# Modified Shor's algorithm using the g^(r/2) ± 1 = mN formula
def shors_algorithm(n):
    # Ensure n is not a prime number or a power of a prime
    if is_prime(n) or math.log(n, 2).is_integer():
        return f"{n} is either prime or a power of a prime. Cannot factorize."

    # Retry with different random values of 'a'
    for _ in range(10):  # Limit to 10 attempts
        a = random.randint(2, n - 1)
        print(f"Randomly chosen 'a': {a}")

        # Step 2: Compute the GCD of 'a' and 'n'
        g = gcd(a, n)
        if g > 1:
            return f"Found a factor using GCD: {g} and {n // g}"

        # Step 3: Find the order 'r' of 'a' modulo 'n'
        r = find_order(a, n)
        if r is None or r % 2 != 0:
            continue  # Skip if 'r' is invalid or not even

        print(f"Order 'r' of {a} modulo {n}: {r}")

        # Step 4: Calculate g^(r/2) ± 1
        g_r_half = pow(a, r // 2)
        factor1 = gcd(g_r_half - 1, n)
        factor2 = gcd(g_r_half + 1, n)

        # Step 5: Check if factors are non-trivial and prime
        if factor1 > 1 and factor1 < n and is_prime(factor1):
            return f"Prime factors of {n} are: {factor1} and {n // factor1}"
        elif factor2 > 1 and factor2 < n and is_prime(factor2):
            return f"Prime factors of {n} are: {factor2} and {n // factor2}"

    return "Pair of prime factors not found."

# Test the program
if __name__ == "__main__":
    number = int(input("Enter a number to factorize: "))
    result = shors_algorithm(number)
    print(result)
