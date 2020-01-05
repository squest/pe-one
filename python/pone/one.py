def p001a():
    sumone = sum(range(3, 1000, 3))
    sumtwo = sum(range(5, 1000, 5))
    sumthree = sum(range(15, 1000, 15))
    return sumone + sumtwo - sumthree


def p001b(x, y, lim):
    def foo(a):
        return (0 == a % x) or (0 == a % y)
    return sum(filter(foo, range(1, lim)))


def fibo(n):
    fibolist = [1, 2]
    a, b = 1, 2
    if n == 1:
        return [1]
    else:
        i = 2
        while i < n:
            c = a + b
            fibolist.append(c)
            a, b = b, c
            i += 1
    return fibolist


def is_even(i):
    return 0 == i % 2


def is_odd(i):
    return 0 != i % 2


def fibolim(lim):
    fibolist = [1]
    a, b = 1, 2
    if b > lim:
        return [1]
    else:
        while b < lim:
            fibolist.append(b)
            c = a + b
            a, b = b, c
    return fibolist

