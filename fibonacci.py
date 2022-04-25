def big_fibonacci(n):
    fibonacci_list = [0,1]
    for i in range(2, n+1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list

print(big_fibonacci(10))

