def flatten(data):
    
    if len(data) == 0:
        data = []
        return data
        

    if isinstance(data[0], list):
        data = flatten(data[0]) + flatten(data = data[1:])
        return data

    else:
        data_1 = [data[0]]
        data = data_1 + flatten(data = data[1:])
        return data


print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))