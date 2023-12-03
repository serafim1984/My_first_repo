from random import randrange
import random


def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity < min or quantity > max:

        new_list = []

        return new_list

    new_list = [random.randint(min, max) for i in range(min, max)]

    new_list = random.sample(new_list, k = quantity)
    
    new_list.sort()
    
    return new_list