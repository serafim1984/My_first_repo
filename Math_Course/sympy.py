
import sympy

#expr = x*x*x/3 + x*x/2 - 2*x
#expr


def compute_derivative(expression, variables, points):
    # Оголошення символьних змінних
    symbols = sympy.symbols(variables)

    # Перетворення рядка у вираз sympy
    expr = sympy.sympify(expression)

    # Обчислення похідної від виразу за вказаними змінними
    derivatives = sympy.diff(expr, symbols)

    # Створення функції, яка може обчислити похідні в точках
    derivative_function = sympy.lambdify(symbols, derivatives, "numpy")

    # Обчислення похідних в заданих точках
    results = derivative_function(points)

    return derivatives, results

# Приклад використання:
expression = "x*x*x/3 + x*x/2 - 2*x"
variables = "x"
points = 1

derivative, derivative_values = compute_derivative(expression, variables, points)
print("Похідні:", derivative)

