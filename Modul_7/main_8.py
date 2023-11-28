import re

def token_parser(s):
    
    list = re.findall('\d+|[+*-//)()]',s)

    return list