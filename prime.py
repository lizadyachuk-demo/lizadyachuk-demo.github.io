def is_prime(n):
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0 or n % 6 == 0 or n % 7 == 0 or n % 8 == 0 or n % 9 == 0:
        return False
    elif n == 1:
        return False
    else:
        return True

print(is_prime(17))

