import math

prime_dict = {}


def ip(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def is_prime(number):
    if number not in prime_dict:
        prime_dict[number] = ip(number)
    return prime_dict[number]


def check(n):
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            y = n // x
            if not is_prime(x + n // x) or not is_prime(y + n // y):
                return False
    return True


with open('w.txt', 'w') as f:
    for i in range(1, 10**7+1):
        if check(i):
            print(i)
            f.write(str(i) + ',')
