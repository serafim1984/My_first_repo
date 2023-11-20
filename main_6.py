CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):

    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    


def translate(name):

    trans_name = ""

    for letter in name:

        if letter == " ":

            trans_name = trans_name + " "

        else: 
            
            trans_name = trans_name + TRANS.get(ord(letter))

    return trans_name