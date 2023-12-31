import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        
        
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        self.contacts = contacts
        if contacts is None:
            contacts = []
        
        

    def save_to_file(self):

        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)
            

    def read_from_file(self):
        with open(self.filename, 'rb') as fh:
            return pickle.load(fh)