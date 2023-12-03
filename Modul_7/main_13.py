def get_employees_by_profession(path, profession):

    with open(path, 'r') as file:
        file_lines = file.readlines()

    list = []

    for line in file_lines:

        if line.find(profession) != -1:

            list.append(line)

    string = ''.join(list)
    string = string.replace('\n', '')
    string = string.replace(profession, '')

    return string[:-1]

print(get_employees_by_profession('Modul_7/list_of_emploees.txt', 'engineer'))