def dice(m, n):
    first = []
    second = []

    for num in range(1, m + 1):
        first.append(num)
    for num in range(1, n + 1):
        second.append(num)

    counter = 0
    if len(second) > len(first):
        for i in second:
            result = 10 - i
            for j in first:
                if result == j:
                    counter += 1
    else:
        for i in first:
            result = 10 - i
            for j in second:
                if result == j:
                    counter += 1

    if counter == 1:
        return "There is {} way to get the sum 10".format(counter)
    return "There are {} ways to get the sum 10".format(counter)


print(dice(12, 4))
print(dice(9, 1))

