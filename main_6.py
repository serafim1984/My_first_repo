import re

def is_spam_words(text, spam_words, space_around=False):

    text = text.lower()

    if space_around == False:

        for word in spam_words:

            if word in text:

                return True

    else:

         for word in spam_words:

            if re.search(' ' + word + ' ', text):

                return True       

            

    return False