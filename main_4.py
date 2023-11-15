def format_ingredients(items):

    try:
        
        recepe = items[0]

    except:

        return ""
    
    for item in items[1:-1:]:

        
        recepe = recepe + f", {item}"


    return recepe + f" and {items[-1]}" if len(items) > 1 else recepe

print(format_ingredients([]))
