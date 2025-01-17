import math

Q = int(input())


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    sqrt_num = math.floor(math.sqrt(num))
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False

    return True


for _ in range(Q):
    print(["No", "Yes"][is_prime(int(input()))])
