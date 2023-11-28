def solve_riddle(riddle, word_length, start_letter, reverse=False):

    word = ''

    if reverse: 

        for letter in riddle[::-1]:

            if letter == start_letter:

                word = riddle[riddle.index(letter) : riddle.index(letter) - word_length : -1]

            else: 
                
                continue

    else:

        for letter in riddle:

            if letter == start_letter:

                word = riddle[riddle.index(letter) : riddle.index(letter) + word_length]

            else: 
                
                continue

    return word

print(solve_riddle('mi1powperet', 3, 'r', True))