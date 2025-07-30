# Tower Breakers


def towerBreakers(n, m):
    return 2 - int(m != 1) * (n % 2)
