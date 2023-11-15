points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):

    sum = 0

    j = 0

    for i in coordinates:

        j = j + 1
    
        if j < len(coordinates):

            if i < coordinates[j]:

                for k, l in points.items():

                    if k == (i, coordinates[j]):

                        sum = sum + l
                        
                        break

            else:

                for k, l in points.items():

                    if k == (coordinates[j], i):

                        sum = sum + l
                        
                        break



    return sum

print(calculate_distance((0, 1, 2, 3)))
