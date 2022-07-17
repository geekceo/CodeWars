import string

def to_camel_case(text):
    if text != '':
        a = [c for c in list(text.title()) if c in string.ascii_letters]
        if list(text)[0].islower(): a[0] = a[0].lower()
        return ''.join(a)
    return ''