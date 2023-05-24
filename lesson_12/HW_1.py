import argparse
import math


def solve_quadratic_equation(a, b, c):

    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        raise ValueError("The equation has no real roots")


def main():
    parser = argparse.ArgumentParser(description='Quadratic Equation Solver')
    parser.add_argument('-a', type=float, default=0, help="coefficient 'a' (default: 0)")
    parser.add_argument('-b', type=float, required=True, help="coefficient 'b'")
    parser.add_argument('-c', type=float, required=True, help="coefficient 'c'")

    args = parser.parse_args()

    try:
        solutions = solve_quadratic_equation(args.a, args.b, args.c)

        if solutions is None:
            print('The equation has no real roots')
        elif isinstance(solutions, tuple):
            x1, x2 = solutions
            print('Roots of the equation: x1 =', x1, 'and x2 =', x2)
        else:
            x = solutions
            print('The equation has one repeated root: x =', x)
    except ValueError as e:
        print('Error:', str(e))


if __name__ == '__main__':
    main()
