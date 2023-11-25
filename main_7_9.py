def is_equal_string(utf8_string, utf16_string):

    utf16_string_candidate = utf8_string.decode('utf8').encode('utf-16')

    if utf16_string_candidate == utf16_string:

        return True

    else:

        return False