def is_valid_pin_codes(pin_codes):
   
    if len(pin_codes) == 0:

        return False

    for pin_code in pin_codes:

        if len(pin_code) != 4 and type(pin_code) == str:

            return False

    for pin_code in pin_codes:

        j = pin_codes.index(pin_code) + 1

        if pin_code in pin_codes[j::]:

            return False

    for pin_code in pin_codes:

        for letter in pin_code:

            if 48 > ord(letter) or ord(letter) > 57:

                return False

    
    return True 

print(is_valid_pin_codes(['1101', '9034', '0011']))