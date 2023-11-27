def capital_text(s):

    flag = 1

    s_new = ''

    for l in s:

        if l == ' ':

            s_new = s_new + l

            continue

        elif flag == 1:

            s_new = s_new + l.capitalize()

            flag = 0

        else:

            s_new = s_new + l

        if l == '.' or l == '!' or l == '?':

            flag = 1     

    return s_new