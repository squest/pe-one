def is_prime(p):
    if p < 2:
        return False
    elif p == 2:
        return True
    elif 0 == p % 2:
        return False
    else:
        lim = p ** 1/2
        i = 3
        while i <= lim:
            if 0 == p % i:
                return False
            i += 2
        return True
