# alt + shift + up/down (select several lines up or down and allow to operate several lines)
# symbol. + 2 tabs - output all methods of this class

'''import calendar

calendar.isleap(year) # check if year is leap year

calendar.calendar(2023) # output caledar for 2023

dir(calendar) # output all methods for class calendar

age = int(input('What is your age >>>> '))

age = 23

type(age) is int

isinstance(age, int)  # check if age is int'''

# kebab-case, snake_case, camelCase, PascalCase

# Ctrl + left click - shows how function coded inside Python in C



'''def is_odd(number):
    if number % 2 == 0:
        print(number, "is even")'''


''' n, o, b = (1, 6, "value") # - unpacking of tuple

print(n)

return a, b, c # - retur of several items as a tuple'''

''' a = 0

def a_ch():

    b = 2
    
    a = b

    return a

print(a) ''' # - print 0!!!


# - "nonlocal' used when function in functions, for defining variable not local at second folled function hierarchy - to use variable from one level up zone of visibility

# args = tuple
# kwargs = dict


''' def intro (firstname, **kwargs):
    print(kwargs)

    print("firstname", firstname)

    for key, value in kwargs.items(): # - iterate for key and values
        print (key, value)

intro(firstname = "Olekcsndr", last_name = "Holodetskyi", age = 18, school = "GoIT") '''


# print(__name__)


# help(a.upper) - output description of method upper of string

# ".".join - call of method join from empty string - in this case . will be a joint

# c = "10"

# help(c.isdigit())

# generator - lasy initialisation

# .encode .decode - string methods transform string to bytes and bytes to string

# def copy_file(file: Path): - can define the format - type hinting is not a validation of types it is just hint

# Path from pathlib is a specific type

# __file__ return path of script launch


# Lecture 8

# black - module chech PEP8 rules of written script

# precommit lecture for module 8

# import pytz - library for using timezones (from pip)

# import time    time.sleep(3)   - delay of interpretator - usfull for programs with several strims


# ctrl + shift + p then format document 



















