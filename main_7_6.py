def get_recipe(path, search_id):

    key_list = ['id', 'name', 'ingredients']

    dictionary = None

    with open(path, 'r') as fh:

        list_temp = fh.readlines()

    for string in list_temp:

        if string.find(search_id) != -1:

            new_string = string.replace('\n', '')

            values = new_string.split(',', 2)

            dictionary = dict(zip(key_list, values))

            ingredients = dictionary.get('ingredients')

            split_ingredients = ingredients.split(',')

            dictionary.update({'ingredients' : split_ingredients})

        else: 
            
            continue
            

    return dictionary  