def all_sub_lists(data):

    sublist_list = [[]]

    for i in range(0, len(data)):

        for j in range(0, len(data) - i):

            sublist_list.append(data[j : i + j + 1])

    return sublist_list

print(all_sub_lists([4, 6, 1, 3]))

