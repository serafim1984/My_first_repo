import re

def total_salary(path):

    sum = 0.0

    salaries = []

    fh = open(path, 'r')
    
    lines = fh.readlines()

    for line in lines:

        sl = re.findall(r"\d+", line)
    
        salaries.append(sl.pop())

    for salary in salaries:
        
        sum = sum + float(salary)

    fh.close()

    return sum