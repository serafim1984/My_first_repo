from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    getcontext().prec = signs_count
    
    sum = Decimal(0)

    for number in number_list:

        sum = sum + Decimal(number)

    avarage = sum / Decimal(len(number_list))

    return avarage