def all_sub_lists(data):

    sublist_list = [[]]

    for item in data:

        i = data.index(item)

        for i in range(data.index(item), len(data)):

            sublist_list.append(data[data.index(item) : i])

    return sublist_list

print(all_sub_lists([1, 2, 3]))

