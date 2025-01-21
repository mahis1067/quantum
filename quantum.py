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

# Function to find factors using g^(r/2) ± 1 method
def factor_with_r(a, n, max_r=100):
    r = 2  # Start with the smallest even value for r
    while r <= max_r:
        # Compute g^(r/2) modulo n
        g_r_half = pow(a, r // 2, n)

        # Calculate g^(r/2) ± 1
        factor1 = gcd(g_r_half - 1, n)
        factor2 = gcd(g_r_half + 1, n)

        # Check if factor1 or factor2 is a valid factor
        if 1 < factor1 < n and n % factor1 == 0:
            if is_prime(factor1) and is_prime(n // factor1):  # Ensure both factors are prime
                return factor1, n // factor1
        if 1 < factor2 < n and n % factor2 == 0:
            if is_prime(factor2) and is_prime(n // factor2):  # Ensure both factors are prime
                return factor2, n // factor2

        # Increment r to the next even number
        r += 2

    return None  # No factors found

# Modified Shor's algorithm
def shors_algorithm(n):
    # Ensure n is not a prime number or a power of a prime
    if is_prime(n) or math.log(n, 2).is_integer():
        return None  # No factors found

    # Retry with different random values of 'a'
    for _ in range(10):  # Limit to 10 attempts
        a = random.randint(2, n - 1)  # Pick a random 'a' value
        print(f"Trying a = {a}")  # Debugging line to observe chosen 'a'

        # Compute the GCD of 'a' and 'n'
        g = gcd(a, n)
        if g > 1 and g < n:
            if is_prime(g) and is_prime(n // g):
                return g, n // g

        # Try to find factors using g^(r/2) ± 1
        result = factor_with_r(a, n)
        if result:
            return result

    return None

while True:

    if __name__ == "__main__":
        number = int(input("Enter a number to factorize: "))
        result = shors_algorithm(number)
        if result:
            print(result)  # Output the pair of prime factors
        else:
            print("No prime factors found.")
