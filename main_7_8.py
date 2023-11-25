def save_applicant_data(source, output):

    with open(output, 'w') as output:
    
        for student in source:

            student_list = []
            for value in student.values():
                student_list.append(str(value))

            output_str = ','.join(student_list)
            
            output.write(output_str + '\n')