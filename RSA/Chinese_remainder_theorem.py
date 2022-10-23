from Extended_Euclid_Algorithm import ext_euc


def chin_rem(p, q, c, e):
    n = p * q

    gcd, d, y = ext_euc(e, (p - 1) * (q - 1))  # упрощение для d*e=1mod(phi(n))
    d = d % ((p - 1) * (q - 1))  # записываем новое значение d
    print(f"value of d = {d}")

    dp = d % (p - 1) # остаток от деления на р-1
    dq = d % (q - 1) # остаток от деления на q-1

    mp = pow(c, dp) % p # шифротекст в степень остатка по модулю р
    mq = pow(c, dq) % q # шифротекст в степень остатка по модулю q

    gcd, yp, yq = ext_euc(p, q) # расширенный Евклида

    m = (mp * yq * q + mq * yp * p) % n # сообщение
    return m


print(chin_rem(619, 971, 362356, 17))
