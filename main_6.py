import re


def replace_spam_words(text, spam_words):

    new_text = text
    
    for word in spam_words:
    
        new_text = re.sub(word, '*' * len(word), new_text, flags = re.IGNORECASE)

    return new_text

