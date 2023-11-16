import sys


def parse_args():
    result = ""

    arglst = sys.argv
    
    for arg in arglst[1:]:

        if arglst.index(arg) == 1:

            result = arg

        else:

            result = result + " " + arg
        
    return result

print(parse_args())