def move_zeros(lst):
    return [*[i for i in lst if i != 0], *[i for i in lst if i == 0]]