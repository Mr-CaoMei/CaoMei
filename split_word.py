import re


def split(addr, word):
    with open(addr, 'r', encoding="utf-8") as flie:
        split_case = flie.readlines()
        for line in split_case:
            if word in line[0]:
                line = re.sub('\s+', '', line)
                return line
    return word
