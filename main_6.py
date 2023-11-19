def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):

    list_JP = []

    list_SG = []

    list_TW = []

    list_UA = []

    dict = {}
    

    for phone in list_phones:

        phone = sanitize_phone_number(phone)

        if phone.startswith("81"):

            list_JP.append(phone)

        elif phone.startswith("65"):

            list_SG.append(phone)

        elif phone.startswith("886"):

            list_TW.append(phone)

        else: 

            list_UA.append(phone)

    dict = {"UA" : list_UA, "JP" : list_JP, "TW" : list_TW, "SG" : list_SG}

    return   dict



print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))   