grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):

    i = 0

    list = []
    
    for name, grd in students.items():

        i += 1

        list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(i, name, grd, grades.get(grd)))


    return list