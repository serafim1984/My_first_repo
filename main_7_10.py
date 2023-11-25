def save_credentials_users(path, users_info):

    with open(path, 'wb') as coded_user_info:

        for user, password in users_info.items():

            coded_user_info.write(user.encode() + ':'.encode() + password.encode() + '\n'.encode())