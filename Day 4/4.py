import re


def scratchcard(card: str):
    split_regex = r"(?:\d+\s+)+\d+|\d+"
    _id, wins, nums = re.findall(split_regex, card)

    find_regex = r"\b(?:" + re.sub("\s+", "|", wins) + r")\b"
    matches = len(re.findall(find_regex, nums))

    return matches


def points(cards: list[str]):
    result = 0
    for card in cards:
        result += int(2 ** (scratchcard(card) - 1))
    return result


def n_copies(cards: list[str]):
    copies = {x: 1 for x in range(len(cards))}

    for index, card in enumerate(cards):
        matches = scratchcard(card)

        for i in range(index + 1, index + matches + 1):
            copies[i] += copies[index]

    return sum(copies.values())


with open("Day 4/input", "r") as f:
    cards = f.readlines()
    print(points(cards))
    print(n_copies(cards))
