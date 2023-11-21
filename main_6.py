def formatted_numbers():

    list = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
    
    for i in range(16):

       

        list.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
        
    return list


for el in formatted_numbers():
    print(el)