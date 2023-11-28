def data_preparation(list_data):

    sanitized_list = []

    for list in list_data:

        if len(list) > 2:

            list.sort()

            list.pop(len(list) - 1)

            list.pop(0)

            sanitized_list.extend(list)

        else:

            sanitized_list.extend(list)

    sanitized_list.sort(reverse = True)

    return sanitized_list