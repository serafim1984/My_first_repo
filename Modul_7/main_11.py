def sequence_buttons(string):

    trans_dict = {1: ['.', ',', '?', '!', ':'], 2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z'], 0: [' ']}

    translate = {}

    for key, value in trans_dict.items():

        for let in value:
    
            translate.update({let : str(key) * (value.index(let) + 1)})

            translate.update({let.lower() : str(key) * (value.index(let) + 1)})

    translate_tab = string.maketrans(translate)
    
    translated_string = string.translate(translate_tab)

    return translated_string

print(sequence_buttons('Hi there!'))
