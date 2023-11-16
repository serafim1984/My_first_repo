# в список можна класти будь які єлементи навіть вбудовані функції

l = [1, 2.2, "Rome", False, None, min, max]


# methods

l.sort()

l.append()

l.count() # рахує скільки є включень якогось єлемента

l.remove()

l.pop()

l.insert # вставляе єлемент перед вказаним єлементом (перишим передається позиція а другим саме значення)

4 in l  # перевіряє чи входить компонент до списку

l.index # перевіряє чи є такий єлемент на вказанній позиції

a = [34, 58]

b = l + a # конкентенація списків

l.extend([1, 2, 3]) # додає список у кінець списка - можна додавати будь який ітерований об'єкт

l.reverse()

l.clear()


a[::-1] # розгортає рядок (у рядка немає метода реверс)

a[-2] # індексація з від'ємними індексами працює

a.split(",") # розбиває рядок на основі вказанного роздільника



a.sort(key=len) # сортування по довжині



''' множини - set'''

''' s = {2, 3, 'home'} - зберігає унікальні елементи причому 1 і 0 пайтон рахує ідентичними з True and False

s.add() - method add value to set

s.remove() - delete element from set - but give exeption when such element do not exist

s.discard() - similar to remove but do not give exeption when such element do not exist

new_list = list(some_set) - change set to list

new_set = set(some_list) - change list to set

-, ^, &,  - працює тільки для множин

| = pipe зклеює дві множини

callable - means function

import os
import sys  allow to work with operation system

print(sys.argv) - save all arguments can be used to put in code parameters inputed in console. practically used for console scripts for devops or smth else


parser.add_argument


'''







