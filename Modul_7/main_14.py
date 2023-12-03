def to_indexed(source_file, output_file):

    with open(source_file, 'r') as source:
        initial_list = source.readlines()

    new_list = []

    for line in initial_list:
        new_line = str(initial_list.index(line)) + ": " + line
        new_list.append(new_line)

    with open(output_file, 'w') as output:
        output.writelines(new_list)