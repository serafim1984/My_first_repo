def split_list(grade):

    sum = 0

    low_grade  = []

    high_grade = []

    for i in grade:
        
        sum = sum + i

    try:
    
       avr = sum / len(grade)

    except:

        return low_grade, high_grade

    for i in grade:

        if i <= avr:

            low_grade.append(i)

        else: 

            high_grade.append(i)  

    return low_grade, high_grade


print(split_list([5, 4, 5, 3, 3, 4, 5, 2, 1, 2]))
