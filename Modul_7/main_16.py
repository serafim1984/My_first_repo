def decode(data):

    data_new = []
    
    if len(data) == 0:
        return data_new

    for i in range(1, data[1] + 1):
        new_data = data_new.append(data[0]) 
        
    data_new = data_new + decode(data[2:])

    return data_new

print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))