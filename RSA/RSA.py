from Extended_Euclid_Algorithm import ext_euc  # расширенный алгоритм Евклида


def fast_pow(m, e, n):  # быстрое возведенеие в степень
    if e == 0:  # если степень 0 то 1
        return 1
    if e == -1:  # если степнь -1 то 1/число
        return 1. / m
    p = fast_pow(m, e // 2, n)  # Целочисленное деление двух чисел //
    p *= p
    if e % 2:
        p *= m
    return p % n


def encryption(e, n, message):
    cipher = ""  # открытый текст определяется пустым

    for c in message:  # проходим по сообщению
        m = ord(c)  # берем кодировку
        cipher = cipher + str(fast_pow(m, e, n)) + " "  # шифр = строка(быстрое возведение m в степень е  по модклю n
    return cipher


def decryption(d, n, cipher):
    message = ""  # открытый текст определяется пустым
    characters = cipher.split()  # разбиваем по смивольно чтобы не было конфузии
    for i in characters:
        c = int(i)  # преобразование текста в целое число,
        message = message + chr(fast_pow(c, d, n))  # текст = строка(быстрое возведение с в степень d  по модклю n
    return message


def generate_key(p, q, e):  # генерируем ключи
    n = p * q
    phiN = (p - 1) * (q - 1)  # функция эйлера
    gcd, d, y = ext_euc(e, phiN)  # d * e = 1 mod (phi(n)) отсюда находим d
    d = d % ((p - 1) * (q - 1))  # записываем новое значение d

    message = "Veronica Gavrilova"
    x = encryption(e, n, message)
    y = decryption(d, n, x)

    print(f"d = {d}")
    print(f"e = {e}")
    print(f"n = {n}")
    print(f"text = {message}")
    print(f"encrypted value of text = {x}")
    print(f"decrypted value of text = {y}")


generate_key(619, 971, 17)  # p, q, e
