a = -10
b = -10

class WidthError(ValueError):
    pass

class HeightError(ValueError):
    pass

# if a != b:
        
#    raise ValueErrror("A != B")

try:
    if a < 0:
        raise WidthError("Error")
    
except ValueError:

    print("Error while checking")

try:
    if b < 0:
        raise HeightError("Error!")
    
except ValueError:

    print("Error while checking")


'''
several messages for error

def input_error(error):
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                print(error)
        return inner
    return error_handler'''