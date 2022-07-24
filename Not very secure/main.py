from string import ascii_letters

def alphanumeric(password):
    return not False in [i in ascii_letters or i in ''.join([str(i) for i in range(0, 10)]) for i in password] if password else False