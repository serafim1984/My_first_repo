import re


def find_word(text, word):

    match_res = re.search(word, text)

    
    
    if match_res:

         dict = {'result' : True, "first_index" : match_res.span()[0], "last_index" : match_res.span()[1], 'search_string' : word, 'string' : text}

    else:

         dict = {'result' : False, "first_index" : None, "last_index" : None, 'search_string' : word, 'string' : text}


    return dict