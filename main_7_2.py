def write_employees_to_file(employee_list, path):

    fh = open(path, 'w')

    for department in employee_list:

        for employee in department:

            fh.write(employee + "\n")

            

    fh.close()