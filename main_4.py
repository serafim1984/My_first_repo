from random import randint


def get_random_password():

    pswr = ""

    for i in range(8):
    
        pswr = pswr + chr(randint(40,126))

    return pswr