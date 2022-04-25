# Defenition of a prime number
def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0 or n % 6 == 0 or n % 7 == 0 or n % 8 == 0 or n % 9 == 0:
        return False
    elif n == 1:
        return False
    else:
        return True

# Function to print primes below a certain number
def primes_below(m):
    for i in range(0, m):
        if is_prime(i):
            print(i, end = " ")

print(primes_below(25))