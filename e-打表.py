import math

prime_dict = {}


def is_prime(number):
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


def factor(n):
    result = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            y = n // x
            result.append(x)
            result.append(y)
    return result


def check(n):
    check_list = [i + n / i for i in factor(n)]
    for i in check_list:
        if i in prime_dict:
            return prime_dict[i]
        if not is_prime(i):
            prime_dict[i] = False
            return False
    prime_dict[i] = True
    return True


with open('w.txt', 'w') as f:
    for i in range(1, 10**7+1):
        if check(i):
            print(i)
            f.write(str(i) + ',')
