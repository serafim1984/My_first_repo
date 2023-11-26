import shutil

def create_backup(path, file_name, employee_residence):

    with open(path + '/' + file_name, 'wb') as file:

        for name, country in employee_residence.items():

            line = name + ' ' + country + '\n'

            file.write(line.encode())


    archive = shutil.make_archive('backup_folder', 'zip', path)
    
    return archive   