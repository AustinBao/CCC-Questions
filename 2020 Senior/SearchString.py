from itertools import permutations

string1 = str(input())
string2 =  str(input())


def factorial(number):
    product = 1
    for i in range(number):
        product *= (i + 1)
    return product


def repeats(needle):
    all_letters = {}
    for i in needle:
        if i not in all_letters:
            all_letters[i] = 1
        else:
            all_letters[i] += 1

    counter = 1
    for keys in all_letters:
        if all_letters[keys] > 1:
            counter *= all_letters[keys]

    return counter


def makePermutations(needle):
    list_of_perms = []

    # Learn how to make custom permutations function
    perm = permutations(needle, len(needle))

    for i in list(perm):
        if i not in list_of_perms:
            list_of_perms.append(i)

    return list_of_perms


def body(needle, haystack):
    repeat_letters = repeats(needle)
    num_of_perms = int(factorial(len(needle)) / repeat_letters)

    all_perms = []
    for tup in makePermutations(needle):
        temp = ""
        for letter in tup:
            temp += letter
        all_perms.append(temp)

    counter = 0
    for perms in all_perms:
        if len(perms) == 1:
            return haystack.count(perms)
        elif perms in haystack:
            counter += 1

    return counter


print(body(string1, string2))
