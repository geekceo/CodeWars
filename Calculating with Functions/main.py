def plus(func=None):
    return [plus.__name__, func]

def minus(func=None):
    return [minus.__name__, func]

def times(func=None):
    return [times.__name__, func]

def divided_by(func=None):
    return [divided_by.__name__, func]

def opers(a: list) -> int:
    if 'plus' in a:
        return a[-1] + a[-2]
    if 'minus' in a:
        return a[-1] - a[-2]
    if 'times' in a:
        return a[-1] * a[-2]
    if 'divided_by' in a:
        return int(a[-1] / a[-2])

def zero(func=None):
    if func == None:
        return 0
    (a:=func).append(0)
    return opers(a)

def one(func=None):
    if func == None:
        return 1
    (a:=func).append(1)
    return opers(a)

def two(func=None):
    if func == None:
        return 2
    (a:=func).append(2)
    return opers(a)

def three(func=None):
    if func == None:
        return 3
    (a:=func).append(3)
    return opers(a)

def four(func=None):
    if func == None:
        return 4
    (a:=func).append(4)
    return opers(a)

def five(func=None):
    if func == None:
        return 5
    (a:=func).append(5)
    return opers(a)

def six(func=None):
    if func == None:
        return 6
    (a:=func).append(6)
    return opers(a)

def seven(func=None):
    if func == None:
        return 7
    (a:=func).append(7)
    return opers(a)

def eight(func=None):
    if func == None:
        return 8
    (a:=func).append(8)
    return opers(a)

def nine(func=None):
    if func == None:
        return 9
    (a:=func).append(9)
    return opers(a)