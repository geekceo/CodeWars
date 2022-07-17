import math

def get_middle(s):
    i = math.floor(len(s)/2)
    return list(s)[i] if len(s) % 2 != 0 else ''.join([list(s)[i - 1], list(s)[i]])