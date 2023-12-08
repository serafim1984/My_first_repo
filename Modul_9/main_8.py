def get_emails(list_contacts):

    emails_list = []

    for i in map(lambda x: x['email'], list_contacts):
        emails_list.append(i)
      

    return emails_list