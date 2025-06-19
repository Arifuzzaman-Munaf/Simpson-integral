# Constants
PI = 3.141592653589793
E = 2.718281828459045
TOLERANCE = 1e-10


def generalize_symbolic_expression(func_str):
    """
    Generalize the user input expression as a computer-recognized function string.
    Args: func_str: Functional expression as a string.
    Returns: Generalized function string for computer evaluation.
    """
    func_str = handle_absolute_functions(func_str)  # handles functions with absolute value notation
    func_str = func_str.replace("^", "**")
    computational_expression = []
    for i in range(len(func_str)):
        computational_expression.append(func_str[i])
        if i < len(func_str) - 1:
            curr = func_str[i]
            nxt = func_str[i + 1]
            if (curr.isdigit() or curr == '.' or curr == ')') and (nxt.isalpha() or nxt == '('):
                computational_expression.append('*')
    return "".join(computational_expression)


def reduce_angle(x):
    """
    Reduce angle x into the interval [-pi, pi].
    Args: x: Angle in radians.
    Returns: Reduced angle in radians.
    """
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    return x


def handle_absolute_functions(expression):
    """
    Convert absolute value notation written with vertical bars into Python's abs() function.
    Args: expression: Input mathematical expression.
    Returns: Expression with Python's abs() absolute value notation.
    """
    result = []
    in_abs = False
    for char in expression:
        if char == '|':
            if not in_abs:
                result.append("abs(")
                in_abs = True
            else:
                result.append(")")
                in_abs = False
        else:
            result.append(char)
    if in_abs:  # In case of an unmatched '|'
        result.append(")")
    return "".join(result)


def sin(x):
    """
    Compute sin(x) using its Taylor series approximation.
    Args: x: Angle in radians.
    Returns: Approximate sin(x) value.
    """
    x = reduce_angle(x)
    term = x
    sin_x = x
    for n in range(1, 15):
        term *= -x * x / ((2 * n) * (2 * n + 1))
        sin_x += term
    return sin_x


def cos(x):
    """
    Compute cos(x) using its Taylor series approximation.
    Args: x: Angle in radians.
    Returns:Approximated cos(x) value.
    """
    x = reduce_angle(x)
    term = 1.0
    cos_x = 1.0
    for n in range(1, 15):
        term *= -x * x / ((2 * n - 1) * (2 * n))
        cos_x += term
    return cos_x


def sec(x):
    """
    Compute secant -> (1/cos(x)).
    Args: x: Angle in radians.
    Returns: Approximated sec(x) value or infinity if undefined.
    """
    cos_x = cos(x)
    if abs(cos_x) < TOLERANCE:
        return float('inf')
    return 1 / cos_x


def cosec(x):
    """
    Compute cosecant ->(1/sin(x)).
    Args: x: Angle in radians.
    Returns: Approximated cosec(x) value or infinity if undefined.
    """
    sin_x = sin(x)
    if abs(sin_x) < TOLERANCE:
        return float('inf')
    return 1 / sin_x


def cot(x):
    """
    Compute cotangent ->(cos(x)/sin(x)).
    Args: x: Angle in radians.
    Returns: Approximated cot(x) value or infinity if undefined.
    """
    sin_x = sin(x)
    if abs(sin_x) < TOLERANCE:
        return float('inf')
    return cos(x) / sin_x


def log(x, max_iterations=100):
    """
    Compute the natural logarithm using a series expansion transformation.
    ln(x) = 2 * (u + u^3/3 + u^5/5 + ...), where u = (x - 1)/(x + 1)

    Args:
        x: Value for which logarithm is computed.
        max_iterations: Maximum iterations for convergence.
    Returns:
        Approximated logarithm of x.
    Raises:
        ValueError: If x is not positive.
    """
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    u = (x - 1) / (x + 1)
    result = u
    u_power = u
    n = 1
    for _ in range(max_iterations):
        n += 2
        u_power *= u * u
        term = u_power / n
        if abs(term) < TOLERANCE:
            break
        result += term
    return 2 * result


def exponential(x, terms=50):
    """
    Compute the exponential function e^x using Taylor series.
    Args:
        x: Power to which e is raised.
        terms: Number of terms in the series.
    
    Returns:
        Approximated e^x value.
    """
    result = 1.0
    term = 1.0
    for n in range(1, terms):
        term *= x / n
        result += term
    return result


def sqrt(x, max_iterations=100):
    """
    Compute the square root of x using Newton-Raphson method.
    Args:
        x: Non-negative value.
        max_iterations: Maximum iterations for convergence.
    Returns:
        Approximated square root of x.
    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0.0
    # Choose an initial guess: if x is 1 or greater, use x; otherwise, use 1.0 (for 0 < x < 1)
    guess = x if x >= 1 else 1.0
    # Iterate using the Newton-Raphson method
    for _ in range(max_iterations):
        new_guess = (guess + x / guess) / 2  # Compute a new approximation using the formula
        # Check for convergence: if the improvement is smaller than the tolerance, return the current estimate
        if abs(new_guess - guess) < TOLERANCE:
            return new_guess
        guess = new_guess  # Update the guess for the next iteration
    return guess


def arc_sin(x, max_iterations=50):
    """
    Compute sin^-1(x) using its Taylor series approximation.
    Args:
        x: Input value in the domain [-1, 1].
        max_iterations: Maximum iterations for convergence.
    Returns:
        Approximated sin^-1(x) value in radians.
    Raises:
        ValueError: If |x| > 1.
    """
    if x < -1 or x > 1:
        raise ValueError("asin(x) undefined for |x| > 1.")
    result = x
    term = x
    iteration = 1
    while iteration < max_iterations:
        term *= ((2 * iteration - 1) ** 2 * x * x) / ((2 * iteration) * (2 * iteration + 1))  # Taylor series expansion
        result += term
        if abs(term) < TOLERANCE:
            break
        iteration += 1
    return result


def arc_tan(x, max_iterations=100):
    """
    Compute tan^-1(x) using its Taylor series approximation for |x| > 1
    Args:
        x: Input value radian.
        max_iterations: Maximum iterations for convergence.
    Returns:
        Approximated tan^-1(x) value in radians.
    """
    if abs(x) > 1:
        if x > 0:
            return PI / 2 - arc_tan(1 / x, max_iterations)  # For positive x, compute via complementary angle
        else:
            return -PI / 2 - arc_tan(1 / x, max_iterations)  # For negative x, adjust sign accordingly
    result = 0.0  # Initialize the result for the Taylor series
    for n in range(max_iterations):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)  # Calculate the nth term of the series
        result += term  # Add the term to the result
        if abs(term) < TOLERANCE:
            break  # Stop if the term is small enough for convergence
    return result  # Return the approximated arctan(x) value


def arc_cos(x, max_iterations=50):
    """
    Compute cos^-1(x) using the relation: acos(x) = pi/2 - asin(x).
    Args:
        x: Input value in the domain [-1, 1].
        max_iterations: Maximum iterations for convergence.
    Returns:
        Approximated cos^-1(x) value in radians.
    Raises:
        ValueError: If |x| > 1.
    """
    if x < -1 or x > 1:
        raise ValueError("acos(x) undefined for |x| > 1.")
    return PI / 2 - arc_sin(x, max_iterations)


def get_custom_functions():
    """
    Returns a dictionary of function names and corresponding functions for use in the evaluation function.
    Returns:
        A dictionary with customized functions.
    """
    return {
        "sin": sin,
        "cos": cos,
        "tan": lambda x: sin(x) / cos(x) if abs(cos(x)) > TOLERANCE else float('inf'),
        "sec": sec,
        "cosec": cosec,
        "csc": cosec,
        "cot": cot,
        "asin": arc_sin,
        "acos": arc_cos,
        "atan": arc_tan,
        "sqrt": sqrt,
        "log": log,
        "ln": log,
        "exp": exponential,
        "pi": PI,
        "e": E,
        "abs": abs,
        }


def evaluate_function(func_str, x_value):
    """
    Evaluate the generalized function string at a given value of x.
    Args:
        func_str: generalized function from a symbolic expression string representing f(x).
        x_value: The value for variable x.
    Returns:
        The result of evaluating the function.
    Raises:
        ValueError: If evaluation fails.
    """
    try:
        custom_functions = get_custom_functions()
        custom_functions["x"] = x_value  # set function value for x
        return eval(func_str, custom_functions)
    except Exception as exc:
        raise ValueError("Error evaluating function at x={}: {}".format(x_value, exc))


def simpsons_rule(func_str, a, b, subdivisions=100):
    """
    Compute the definite integral of f(x) from a to b using Simpson's Rule.
    Args:
        func_str: Generalized function string representing f(x).
        a: Lower limit of integration.
        b: Upper limit of integration.
        subdivisions: Number of subdivisions (must be even)
    Returns:
        Approximated definite integral.
    """
    if subdivisions % 2 != 0:
        subdivisions += 1  # make even in case of odd input
    h = (b - a) / subdivisions  # step size
    total = evaluate_function(func_str, a) + evaluate_function(func_str, b)  # endpoints
    for i in range(1, subdivisions):
        x = a + i * h  # current x
        weight = 4 if i % 2 != 0 else 2  # Simpson weight
        total += weight * evaluate_function(func_str, x)  # accumulate weighted value
    return (h / 3) * total  # Simpson's rule result


def main():
    print("Simpson's Rule Numerical Integration")
    print("-----------------------------------")
    raw_function = input("Enter the function f(x) : \n"
                         "(Input Example:\n sin(x) + cos(x), log(2x+3),\n asin(x) + acos(x) where 'a' means arc,\n"
                         " 2x/(4x^2 + 1), (x^2 + 2x +3)/|2x-3| ...etc) \n==>")
    try:
        a = float(input("Enter the lower limit of integration (a): "))
        b = float(input("Enter the upper limit of integration (b): "))
    except ValueError:
        print("Invalid number. Please enter numeric values for the limits.")
        return

    generalized_function = generalize_symbolic_expression(raw_function)
    try:
        result = simpsons_rule(generalized_function, a, b)
        print("\nThe approximate integral of f(x) from {} to {} is: {:.6f}".format(a, b, result))
    except Exception as err:
        print("\nAn error occurred: {}".format(err))


def exit_program():
    if input("Press enter to exit the program:"):
        exit()


if __name__ == "__main__":
    main()
    exit_program()
