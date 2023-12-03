import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
  
    my_cats = []

    if isinstance(cats[0], dict):

        for cat in cats:
  
            my_cats.append(Cat(cat.get('nickname'), cat.get('age'), cat.get('owner')))

        return my_cats
    
    else:

        for cat in cats:

            new_cat = {"nickname" : cat.nickname, "age" : cat.age, "owner" : cat.owner}

            my_cats.append(new_cat)

        return my_cats






    
print(convert_list([
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
])) 


