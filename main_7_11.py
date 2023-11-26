def get_credentials_users(path):

    with open(path, 'rb') as coded_passwords:

        coded_passwords_list = coded_passwords.readlines()

        decoded_list = []

    for line in coded_passwords_list:

        line_decoded = line.decode()
        
        decoded_list.append(line_decoded.replace('\n', ''))       

    return decoded_list