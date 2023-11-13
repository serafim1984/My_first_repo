def prepare_data(data):

    data.sort()

    data.pop(0)
    data.pop(-1)
    

    return data

print(prepare_data([5, 6, 10, 19, 3, 8]))
