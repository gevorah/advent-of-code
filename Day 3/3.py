import re
from functools import reduce


def engine(text: str):
    cols = text.find("\n") + 1
    result = 0
    for value in re.finditer(r"\d+", text):
        left = value.start() - 1
        if left < 0 or text[left] == "\n":
            left += 1

        right = value.end()
        if right >= len(text) or text[right] == "\n":
            right -= 1

        top = list(range(left - cols, right - cols + 1))
        bottom = list(range(left + cols, right + cols + 1))

        search = top + bottom + [left, right]

        for symbol in re.finditer(r"[^\n\.\d]", text):
            if symbol.start() in search:
                result += int(value.group())
                break

    return result


def engine_enhanced(text: str):
    cols = text.find("\n") + 1
    result = 0
    for symbol in re.finditer(r"\*", text):
        left = symbol.start() - 1
        if left < 0 or text[left] == "\n":
            left += 1

        right = symbol.end()
        if right >= len(text) or text[right] == "\n":
            right -= 1

        top = list(range(left - cols, right - cols + 1))
        bottom = list(range(left + cols, right + cols + 1))

        search = top + bottom + [left, right]

        gear = []
        for value in re.finditer(r"\d+", text):
            if value.start() in search or value.end() - 1 in search:
                gear.append(int(value.group()))

        result += reduce((lambda x, y: x * y), gear) if len(gear) == 2 else 0

    return result


with open("Day 3/input", "r") as f:
    text = "".join(f.readlines())
    print(engine_enhanced(text))
