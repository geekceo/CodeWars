def rgb(r, g, b):
    a = list()
    for i in [r, g, b]:
        if i > 255:
            a.append('FF')
        elif i <= 0:
            a.append('00')
        elif 0 < i < 9:
            a.append(f'0{i}')
        else:
            a.append(hex(i).split('x')[-1].upper())

    return ''.join(a)