articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    
    articles = []
      
    for art in articles_dict:

        for k, v in art.items():

            if type(v) != str:

                continue

            if letter_case == False:

                key_1 = key.lower()
                v_1 = v.lower()

                if v_1.find(key_1) != -1:

                    articles.append(art)

                    break

                else: 

                    continue

            else:

                if v.find(key) != -1:

                    articles.append(art)

                    break

                else: 

                    continue
                

    return articles

print(find_articles("Ocean"))
