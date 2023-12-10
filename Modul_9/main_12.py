from functools import reduce


def amount_payment(payment):

    new_list = []
    
    for i in filter(lambda x: x > 0, payment):
        new_list.append(i)
    
    return reduce(lambda x, y: x + y, new_list)