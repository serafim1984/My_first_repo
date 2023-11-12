def fibonacci(n):

    if n == 0:

        f_n = 0

    elif n == 1:

        f_n = 1

    else: 

        f_n = fibonacci(n - 1) + fibonacci(n - 2)

    return f_n

print(fibonacci(5))

      
