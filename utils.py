from math import sqrt
from scipy.integrate import quad


def fact(n):
    """Computes the factorial of a natural number.

    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if not isinstance(n, int):
        raise ValueError("The input is not an int")
    if n < 0:
        raise ValueError("The input is negative")
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.

    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
            to the roots of the ax^2 + bx + c polynomial.
    """
    if not (isinstance(a, int) or isinstance(a, float)) or \
            not (isinstance(b, int) or isinstance(b, float)) or \
            not (isinstance(c, int) or isinstance(c, float)):
        raise ValueError("Some values are not of the type float or int")
    delta = b*b-4*a*c
    if delta < 0 or (delta == 0 and a == 0 and b == 0):
        return ()
    elif delta > 0:
        r1 = (-b+sqrt(delta))/2*a
        r2 = (-b-sqrt(delta))/2*a
        if r1 == r2:
            return (r1)
        else:
            return (r1, r2)
    else:
        return (0) if a == 0 else (-b/(2*a))


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds

    Pre: 'function' is a valid Python expression with x as a variable,
            'lower' <= 'upper',
            'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
            of the specified 'function'.

    Hint: You can use the 'integrate' function of the module 'scipy' and
            you'll probably need the 'eval' function to evaluate the function
            to integrate given as a string.
    """
    if upper < lower:
        raise ValueError(
            "lower value {lower} is greater than upper value {upper}")

    def mathFun(x): return eval(function)

    return quad(mathFun, lower, upper)[0]


if __name__ == '__main__':
    print(fact(5))
    print(roots(1, -2, 1))
    print(integrate('x ** 2 - 1', 1, 2))
