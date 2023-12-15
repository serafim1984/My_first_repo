import csv

contacts = [    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},     {
    "name": "Chaim Lewis",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
},     {
    "name": "Kennedy Lane",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},     {
    "name": "Wylie Pope",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},     {
    "name": "Cyrus Jackson",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
}]


def write_contacts_to_file(filename, contacts):
    with open (filename, 'w', newline = '') as fh:
        field_names = contacts[0].keys()
        writer = csv.DictWriter(fh, fieldnames = field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    with open (filename, 'r', newline = '') as fh:
        
        contacts = csv.DictReader(fh)
        new_contacts =[]

        for contact in contacts:
            contact['favorite'] = bool(contact['favorite'])
            new_contacts.append(contact)

    return new_contacts


write_contacts_to_file('contacts.csv', contacts)

print(read_contacts_from_file('contacts.csv'))