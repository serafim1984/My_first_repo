def is_valid_password(password):

    check_1 = False
    check_2 = False
    check_3 = False
    

    if len(password) < 8:

        return False

    for sym in password:

        if ord(sym) > 65 and ord(sym) < 90:

              check_1 = True

        if ord(sym) > 97 and ord(sym) < 122:

              check_2 = True

        if ord(sym) > 48 and ord(sym) < 57:

              check_3 = True

    return check_1 and check_2 and check_3