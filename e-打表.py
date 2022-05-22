import math
prime_dict = {}


def isPrime(n):
    if n in prime_dict:
        return prime_dict[n]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime_dict[n] = False
            return False
    prime_dict[n] = True
    return True


def factor(n):
    result = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            y = n // x
            result.append(x)
            result.append(y)
    return result


def check(n):
    for i in factor(n):
        if not isPrime(i + n / i):
            return False
    return True


res = []
for i in range(1, 10**7 + 1):
    if check(i):
        res.append(i)
f = open('w.txt', 'w')
f.write(str(res))
f.close()
