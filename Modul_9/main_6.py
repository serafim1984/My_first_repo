import re

def generator_numbers(string=""):
    list = re.findall('\d+',string)
    for i in range(0, len(list)):
        yield int(list[i])

        i = i + 1
        


def sum_profit(string):
    sum = 0
    for number in generator_numbers(string):

        sum = sum + number

    return sum