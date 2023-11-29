def all_sub_lists(data):

    sublist_list = [[]]

    for item in data:

        i = data.index(item)

        for i in range(data.index(item), len(data)):

            sublist_list.append(data[data.index(item) : i + 1])

    return sublist_list

print(all_sub_lists([4, 6, 1, 3]))

