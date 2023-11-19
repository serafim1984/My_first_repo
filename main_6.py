def sanitize_phone_number(phone):
        
    phone = phone.strip()
    phone = phone.replace("+", "")
    phone = phone.replace(")", "")
    phone = phone.replace("(", "")
    phone = phone.replace("-", "")
    phone = phone.replace(" ", "")

    return phone
