def is_integer(s):

    s_new = s.strip()
    
    if len(s) == 0:

        return False

    elif s_new.startswith('+') or s_new.startswith('-'):

        return s_new[1:].isdigit()

    else:

        return s_new.isdigit()