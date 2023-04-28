class DiscriminantError(Exception):
    pass


def solve_quadratic_equation(a, b, c):

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        raise DiscriminantError("Discriminant is negative, equation has no real solutions")

    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)

    return x1, x2


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

try:
    x1, x2 = solve_quadratic_equation(a, b, c)
    print("Solutions: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2))
except DiscriminantError as e:
    print("Error: {}".format(str(e)))
