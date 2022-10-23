def ext_euc(a, b):
    if b == 0:  # пока b не 0
        d, x, y = a, 1, 0  # d = ax + by и d|a и d|b (| побитовое или)
    else:
        d, x1, y1 = ext_euc(b, a % b)  # a становится b, а b становится остатком от a/b
        x = y1  # значения меняются местами для b и a%b
        y = x1 - y1 * (a // b)  # значения меняются местами a=b*q+r q=коэффициент
    return d, x, y
