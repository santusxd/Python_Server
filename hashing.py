from random import seed, choice
from string import ascii_letters, digits, punctuation

choices = ascii_letters + digits + punctuation


def hashing(input):
    seed(input)
    hashed = ""
    # hashed_list = []
    for i in range(64):
        #choices[raindint(0, len(choices))]
        hashed += choice(choices)
        # hashed_list.append(choice(choices)
    return hashed
    # return "".join(hashed_list)


print(choices)
