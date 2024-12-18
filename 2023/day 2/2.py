import re
from functools import reduce


def is_possible(text: str):
    cubes = {"red": 12, "green": 13, "blue": 14}
    game = int(re.findall(r"\d+", text)[0])

    regex = re.compile("\d+\s[%s]+" % "|".join(cubes.keys()))
    values = re.findall(regex, text)

    for x in values:
        count, color = x.split(" ")
        if int(count) > cubes[color]:
            return 0

    return game


def is_possible_enhanced(text: str):
    cubes = {"red": 12, "green": 13, "blue": 14}

    regex = re.compile("\d+\s[%s]+" % "|".join(cubes.keys()))
    values = re.findall(regex, text)

    min_cubes = dict.fromkeys(cubes.keys(), 0)
    for x in values:
        count, color = x.split(" ")
        if int(count) > min_cubes[color]:
            min_cubes[color] = int(count)

    return reduce((lambda x, y: x * y), min_cubes.values())


with open("day 2/input", "r") as f:
    result = 0
    for line in f.readlines():
        result += is_possible_enhanced(line)

    print(result)
