def real_len(text):

    text_1 = text.replace("\n", "")

    text_2 = text_1.replace("\f", "")

    text_3 = text_2.replace("\r", "")

    text_4 = text_3.replace("\t", "")

    text_5 = text_4.replace("\v", "")

    return len(text_5)
