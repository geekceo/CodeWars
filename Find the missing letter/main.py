import string

def find_missing_letter(chars):
    alpha: str
    alpha = string.ascii_uppercase if chars[0].isupper() else string.ascii_lowercase
    for k, v in dict(zip(chars, list(alpha)[list(alpha).index(chars[0]):list(alpha).index(chars[0]) + len(chars)])).items():
        if k != v:
            return v