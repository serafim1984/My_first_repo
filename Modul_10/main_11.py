from collections import UserString


class NumberString(UserString):
    def number_count(self):

        num = 0
        
        for i in self.data:

            if i.isdigit():

                num = num + 1

            else:
                continue

        return num