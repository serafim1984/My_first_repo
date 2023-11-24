def get_cats_info(path):

    key_list = ['id', 'name', 'age']

    list_final = []

    with open(path, 'r') as fh:

        list_temp = fh.readlines()

    for string in list_temp:

        new_string = string.replace('\n', '')

        dict_item = dict(zip(key_list, new_string.split(',')))

        list_final.append(dict_item)

    return list_final