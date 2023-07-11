num = 21


def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


addend1 = 2
while True:
    addend2 = num * 2 - addend1

    if check_prime(addend2) is True:
        print(addend1, addend2)
        exit()
    else:
        addend1 += 1

