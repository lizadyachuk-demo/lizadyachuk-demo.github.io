def solve_quadratic(a,b,c):
    det = b ** 2 - 4 * a * c
    if det < 0:
        return None
    elif det == 0:
        return -b / (2 * a)
    else:
        answer1 = (-b + det ** (1/2)) / (2 * a)
        answer2 = (-b - det ** (1/2)) / (2 * a)
        return (answer1, answer2)

print(solve_quadratic(1,-5, 6))
print(solve_quadratic(1, 4, 4))
print(solve_quadratic(1, 0, 1))