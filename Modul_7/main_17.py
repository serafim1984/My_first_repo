def encode(data):

    data_new = []

    i = 1
    
    if len(data) == 0:
        return data_new

    while (i + 1) <= len(data) and data[0] == data[i]:
        i = i + 1
    
    data_new.append(data[0])
    data_new.append(i)
    
    data_new = data_new + encode(data[i:])

    return data_new

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))