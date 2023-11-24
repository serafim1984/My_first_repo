def read_employees_from_file(path):

    fh = open(path, 'r')
    
    employees = fh.readlines()

    n = len(employees)
    
    fh.close()
    
    employees_str = ''.join(employees)

    new_employees = employees_str.split('\n')

    new_employees = new_employees[:n]

    return new_employees

