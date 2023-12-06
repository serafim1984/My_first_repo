def format_phone_number(func):

    def inner(phone):  

        new_phone = func(phone)
        
        if len(new_phone) == 12:
            formated_phone = '+' + new_phone 
            return formated_phone

        else:

            formated_phone = '+38' + new_phone
            return formated_phone
            
    return inner
            
        
    


@format_phone_number
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