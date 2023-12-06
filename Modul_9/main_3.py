
def caching_fibonacci(): 
    
    cache = {}
    
    def fibonacci(n):

        if cache.get(n):

            return cache.get(n)
            
        f_n = 0

        if n == 0:

            f_n = 0

        elif n == 1:

            f_n = 1

        else: 

            f_n = fibonacci(n - 1) + fibonacci(n - 2)

        cache[n] = f_n
        
        return f_n 

    return fibonacci
