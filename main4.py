firstname = input('Insert your first name here: ')
if len(firstname) < 5:
    lastname = input('Insert your last name here: ')
    data = firstname + lastname
    print(data.upper())
else:
    print(firstname.lower())
