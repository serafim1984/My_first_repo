def get_grade(key):
    
    grades = {"F" : 1, "FX" : 2, "E" : 3, "D" : 3, "C" : 4, "B" : 5, "A" : 5}

    return grades.get(key)


def get_description(key):
    
    grades = {"F" : "Unsatisfactorily", "FX" : "Unsatisfactorily", "E" : "Enough", "D" : "Satisfactorily", "C" : "Good", "B" : "Very good", "A" : "Perfectly"}    

    return grades.get(key)


print(get_grade("A"))

print(get_description("F"))
